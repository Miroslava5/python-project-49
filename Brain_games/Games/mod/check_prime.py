

def do_check_prime(number):
    dividers = list(range(2, number - 1))
    for div in dividers:
        if number % div == 0:
            return 'no'
    return 'yes'


if __name__ == '__main__':
    pass
