import random

flag = list(open("flag.txt", "rb").read().strip())
random.seed(random.randint(0, 256))
random.shuffle(flag)
print(bytes(flag).decode())
