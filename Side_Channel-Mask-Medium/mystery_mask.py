import os
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import numpy as np
import galois

GF256 = galois.GF(256)

def gen_mask():
    y = 0
    while not y:
        y = GF256.Random()
    return y

def mask(inp):
    x = gen_mask()
    y = gen_mask()
    z = gen_mask()
    t = gen_mask()
    return [GF256(inp) / x / y / z / t, x, y, z, t]

def masked_inversion(S):
    output = S
    for i in range(5):
        for j in range(16):
            output[j][i] = GF256(S[j][i]) ** 254
    return output

def make_traces(key, inputs):

    for inp in inputs:
        L = [ mask(inp[i] ^ key[i]) for i in range(16) ]

        # ===== BEGINNING OF THE SIDE CHANNEL TRACE ======= #
        masked_inversion(L)
        # =====   END OF THE SIDE CHANNEL TRACE     ======= #

def encrypt_flag(key):
    iv = os.urandom(16)
    flag = open("../private/flag.txt", "rb").read()
    c = AES.new(bytes(key), AES.MODE_CBC, iv = iv).encrypt(pad(flag, 16))
    return {
        "iv": iv.hex(),
        "c": c.hex(),
    }

def unmask(L):
    a, b, c, d, e = L
    return a * b * c * d * e

def test_implementation():
    for _ in range(100):
        L1 = list(map(GF256, list(os.urandom(16))))
        L2 = masked_inversion([ mask(x) for x in L1 ]) # masked inversion
        L2 = [ unmask(x) for x in L2 ]
        L3 = [ x ** 254 for x in L1 ] # unmasked inversion
        assert L2 == L3

if __name__ == "__main__":

    # Check the correctness of the implementation
    test_implementation()

    # Generate random key and inputs
    key = list(os.urandom(16))
    inputs = [ list(os.urandom(16)) for _ in range(5000) ]

    np.savez_compressed("inputs", inputs = np.array(inputs, dtype = np.uint8))

    # Traces are saved externally and given in traces.npz
    make_traces(key, inputs)

    output = encrypt_flag(key)
    print(output)
