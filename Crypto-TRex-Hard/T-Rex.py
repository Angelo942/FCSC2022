import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class TRex:
	def __init__(self, key):
		N = len(key)
		M = 2 ** (8 * N)
		self.key = key
		self.iv = int.from_bytes(key, "big")
		R = lambda x: ((2 * x + 1) * x)
		for _ in range(31337):
			self.iv = R(self.iv) % M
		self.iv = int.to_bytes(self.iv, N, "big")

	def encrypt(self, data):
		E = AES.new(self.key, AES.MODE_CBC, iv = self.iv)
		return self.iv + E.encrypt(pad(data, 16))

if __name__ == "__main__":
	E = TRex(os.urandom(16))
	flag = open("flag.txt", "rb").read().strip()
	c = E.encrypt(flag)
	print(c.hex())
