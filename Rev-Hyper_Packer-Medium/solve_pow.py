#!/usr/bin/env python3

import subprocess
from pwn import *

HOST = args.HOST or "challenges.france-cybersecurity-challenge.fr"
PORT = args.PORT or  2202

def main():
    r = remote(HOST, PORT)
    _ = r.recvlines(5)

    cmdline = r.recvline().strip().decode("utf-8").split(" ")
    assert cmdline[0] == "hashcash"
    assert cmdline[1] == "-mb26"
    assert cmdline[2].isalnum()

    log.info(f"Solving PoW")
    solution = subprocess.check_output([cmdline[0], cmdline[1], cmdline[2]])
    log.success(f"Solved PoW: {solution.decode()}")

    r.sendline(solution)
    _ = r.recvline()

    encoded = r.recvline().strip()
    binary = b64d(encoded)

    with open("/tmp/hyperpacker.bin", "wb") as fp:
        fp.write(binary)

    log.success("Binary written at /tmp/hyperpacker.bin")

    # Solve the challenge here
    # ...

if __name__ == "__main__":
    main()
