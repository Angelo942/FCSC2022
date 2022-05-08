import os
import json
import hashlib
import string
import numpy as np
from Crypto.Random.random import randint, choice
from Crypto.Hash import SHA512, SHA256
from Crypto.Util.number import bytes_to_long
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

Q = 8383489
B = 16384
N = 512

class Server:
    def __init__(self, Q, B, N):
        self.Q = Q
        self.B = B
        self.N = N
        self.a = [randint(0, Q - 1) for _ in range(self.N)]
        self.__s1 = [randint(-1, 1) % Q for _ in range(self.N)]
        self.__s2 = [randint(-1, 1) % Q for _ in range(self.N)]
        self.t = self.poly_mul_add(self.a, self.__s1, self.__s2)

    def sk(self):
        return self.__s1, self.__s2

    def pk(self):
        return self.a, self.t

    def H(self, v1, m):
        h = bytes_to_long(SHA512.new(str(v1).encode() + m).digest())
        h = list(map(int, list(f"{h:0512b}")))
        return h

    def poly_add(self, p1, p2):
        return [ (p1[i] + p2[i]) % self.Q for i in range(self.N) ]

    def poly_sub(self, p1, p2):
        return [ (p1[i] - p2[i]) % self.Q for i in range(self.N) ]

    def poly_mul_add(self, p1, p2, p3):
        return self.poly_add(self.poly_mul(p1, p2), p3)

    def poly_mul(self, p1,p2):
        res = np.convolve(p1, p2)
        res = [0] * (2 * self.N - 1 - len(res)) + list(res)
        a = list(map(int, res[:self.N]))
        b = list(map(int, res[self.N:] + [0]))
        res = self.poly_sub(a, b)
        return res

    def reject(self, z):
        for v in z:
            if v > self.B and v < self.Q - self.B:
                return True
        return False

    def sign(self, m):
        while True:
            y1 = [ randint(-self.B, self.B) % self.Q for _ in range(self.N) ]
            y2 = [ randint(-self.B, self.B) % self.Q for _ in range(self.N) ]
            h = self.poly_mul_add(self.a, y1, y2)
            c = self.H(h, m)
            z1 = self.poly_mul_add(self.__s1, c, y1)
            z2 = self.poly_mul_add(self.__s2, c, y2)
            if self.reject(z1) or self.reject(z2):
                continue
            return y1, z1, z2, c

    def verify(self, z1, z2, c, m):
        if self.reject(z1) or self.reject(z2):
            return False
        temp1 = self.poly_mul_add(self.a, z1, z2)
        temp2 = self.poly_mul(self.t, c)
        h = self.poly_sub(temp1, temp2)
        c_prime = self.H(h, m)
        return c == c_prime

def get_random_string(length):
    return ''.join(choice(string.ascii_letters) for _ in range(length))

if __name__ == "__main__":

    server = Server(Q, B, N)
    a, t = server.pk()
    print(json.dumps({
        "a": a,
        "t": t,
    }))

    data = []
    for i in range(N):
        message = get_random_string(20)
        y1, z1, z2, c = server.sign(message.encode())
        assert server.verify(z1, z2, c, message.encode()), "Error: verification error."
        data.append({
            "message": message,
            "z1": z1,
            "z2": z2,
            "c": c,
            "y1": y1,
        })
    print(json.dumps(data))

    flag = open("flag.txt", "rb").read()
    s1, s2 = server.sk()
    key = SHA256.new(str(s1).encode() + str(s2).encode()).digest()
    iv = os.urandom(16)
    E = AES.new(key, AES.MODE_CBC, iv = iv)
    enc = E.encrypt(pad(flag, 16))
    print(json.dumps({
        "iv": iv.hex(),
        "enc": enc.hex()
    }))
