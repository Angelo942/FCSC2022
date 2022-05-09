#!/usr/bin/env python3.9
try:
	flag = tuple(open("flag.txt", "rb").read())
	assert len(flag) == 70

	challenge = hash(flag)
	print(f"{challenge = }")

	T = tuple(input(">>> ").encode("ascii"))
	if bytes(T).isascii() and hash(T) == challenge:
		print(flag)
	else:
		print("Try harder :-)")
except:
	print("Error: please check your input")
