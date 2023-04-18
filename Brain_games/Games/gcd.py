import prompt
from random import randint
from Brain_games.Games.check import do_check
from Brain_games.Games.euclidean_algorithm import find_gcd


def do_game_gcd():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        print(f'Question: {number1} {number2}')
        right_answer = find_gcd(number1, number2)
        answer = prompt.integer('Your answer: ')
        if do_check(answer, right_answer) == 'Correct':
            print(do_check(answer, right_answer))
            count += 1
        else:
            print(do_check(answer, right_answer), f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    do_game_gcd()
