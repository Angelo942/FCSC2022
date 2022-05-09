import re

def optimal(t):
	if t == 0:
		return []
	for c in L:
		if c <= t:
			return [c] + optimal(t - c)

def IsBetterThanOptimal(s):
	if sum(s) != t:      return False
	if len(s) >= len(r): return False
	if set(s) > set(L):  return False
	return True

try:
	t = int(input())
	L = sorted(map(int, re.findall("\d+", input())), reverse = True)

	assert t > 0
	assert len(L) >= 1
	r = optimal(t)

	s = list(map(int, re.findall("\d+", input())))
	assert len(s) >= 1

	if IsBetterThanOptimal(s):
		print(open("flag.txt").read().strip())

except:
	print("Check your inputs.")
