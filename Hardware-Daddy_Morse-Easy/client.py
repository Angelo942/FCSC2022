from pwn import *
import numpy as np
import base64

HOST = args.HOST or "challenges.france-cybersecurity-challenge.fr"
PORT = args.PORT or  2251

c = remote(HOST, PORT)

hello_signal = np.fromfile("signal.iq", dtype = np.complex64)

encoded_signal = base64.b64encode(hello_signal.tobytes())

c.recvuntil(b"> ")
c.sendline(encoded_signal)
print(c.recvline())
