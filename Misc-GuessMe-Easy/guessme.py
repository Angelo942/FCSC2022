import os

N = 64
M = 16
success = 0
try:
	for i in range(M):
		secret = int.from_bytes(os.urandom(N // 8), "big")
		for _ in range(N + 1):
			x = int(input(">>> "))
			if secret < x:
				print("-1")
			elif secret > x:
				print("+1")
			elif secret == x:
				print("0")
				print(f"{i+1} found, {M-1-i} more to go")
				success += 1
				break
	if success == M:
		print(open("flag.txt").read())
except:
	pass
