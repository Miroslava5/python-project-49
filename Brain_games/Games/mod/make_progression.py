from random import randint


def make_arithmetic():
    step = randint(1, 50)
    progress_list = list(range(0, 1000, step))
    length = randint(5, 11)
    start = randint(0, len(progress_list) - length)
    cut_list = progress_list[start:start + length]
    return cut_list


if __name__ == '__main__':
    pass
