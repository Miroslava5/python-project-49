import prompt
from random import randint
from Brain_games.Games.mod.check_prime import do_check_prime
from Brain_games.Games.mod.check import do_check


def do_game_prime():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(0, 100)
        right_answer = do_check_prime(number)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if do_check(answer, right_answer) == 'Correct':
            print(do_check(answer, right_answer))
            count += 1
        else:
            print(do_check(answer, right_answer))
            return print(f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    do_game_prime()
