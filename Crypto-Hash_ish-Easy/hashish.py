#!/usr/bin/env python3.9
import os

try:
	flag = open("flag.txt", "rb").read()
	assert len(flag) == 70

	flag = tuple(os.urandom(16) + flag)

	challenge = hash(flag)
	print(f"{challenge = }")

	a = int(input(">>> "))
	b = int(input(">>> "))

	if hash((a, b)) == challenge:
		print(flag)
	else:
		print("Try harder :-)")
except:
	print("Error: please check your input")
