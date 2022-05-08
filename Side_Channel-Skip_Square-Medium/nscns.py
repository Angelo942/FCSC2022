from Crypto.Util.number import getPrime, bytes_to_long

BITS = 256

def exp_mod_skip_squ(x, y, n, skip = -1):
    fmt = f"{{:0{2*BITS}b}}"
    exp = fmt.format(y)

    value = 1
    for i, e in enumerate(exp):
        if skip != i: value *= value
        if e == "1":  value *= x
        value %= n
    return value

if __name__ == "__main__":

    p, q = getPrime(BITS), getPrime(BITS)
    n = p * q
    e = 2 ** 16 + 1
    d = pow(e, -1, (p - 1) * (q - 1))

    print(f"{n = }")
    print(f"{e = }")

    try:
        for _ in range(2 * BITS + 1):
            msg = bytes_to_long(input("msg = ").encode())
            if msg == 0:
                break
            skip = int(input("skip = "))
            print(exp_mod_skip_squ(msg, d, n, skip))
    except:
        print("Please check your inputs.")
        exit(0)

    with open("flag.txt", "rb") as fp:
        m = bytes_to_long(fp.read().strip())
        assert m < n
        c = pow(m, e, n)
        print(f"{c = }")
