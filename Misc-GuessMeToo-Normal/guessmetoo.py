from Crypto.Random.random import getrandbits, randrange

N = 128
C = 136
K =  32

def I():
	try:
		return int(input(">>> "))
	except:
		exit(0)

def w(x):
	return bin(x).count("1") & 1

def game():
	secret = getrandbits(N)
	
	M = [ I() for _ in range(C) ]
	if len(M) != len(set(M)):
		print("Repetitions are not allowed")
		exit(0)

	E = [0] * C
	E[randrange(C)] = 1
	print([ w(m & secret) ^ e for m, e in zip(M, E) ])

	print("Now, can you guess the secret?")
	ch = I() == secret
	if ch:
		print("Well done!")
	else:
		print("Nope.")

	return ch

if __name__ == "__main__":

	flag = open("flag.txt").read()

	G = [ game() for _ in range(K) ]
	if False not in G:
		print(flag)