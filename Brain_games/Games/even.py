import prompt
from random import randint
from Brain_games.Games.check import do_check

def do_game_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(0, 1000)
        print('Question: ', number)
        right_answer = 'yes' if number % 2 == 0 else 'no'
        answer = prompt.string('Your answer: ')
        if do_check(answer, right_answer) == 'Correct':
            print(do_check(answer, right_answer))
            count += 1
        else:
            return print(do_check(answer, right_answer)+ f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    do_game_even()
