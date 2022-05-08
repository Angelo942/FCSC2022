import os
import json
import gmpy2
from fractions import Fraction
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt(n):
	IV = os.urandom(16)
	FLAG = open("flag.txt", "rb").read()

	k = int.to_bytes(n, 32, "big")
	aes = AES.new(k, AES.MODE_CBC, iv = IV)
	ctxt = aes.encrypt(pad(FLAG, 16))
	output = {
		"iv": IV.hex(),
		"ciphertext": ctxt.hex(),
	}
	return output

if __name__ == "__main__":

	try:
		a = Fraction(input(">>> a = "))
		b = Fraction(input(">>> b = "))
		
		c = a ** 2 + b ** 2
		assert gmpy2.is_square(c.numerator)
		assert gmpy2.is_square(c.denominator)
		assert a * b == 20478

		n = int(gmpy2.isqrt(c.numerator))
		
		output = encrypt(n)
		print(json.dumps(output))

	except:
		print("Error: check your inputs.")
