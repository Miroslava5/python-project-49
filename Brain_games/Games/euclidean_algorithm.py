

def find_gcd(a, b):
    while (a != 0) and (b != 0):
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b


if __name__ == '__main__':
    find_gcd()
