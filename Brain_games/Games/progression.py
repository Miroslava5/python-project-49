import prompt
from random import randint
from Brain_games.Games.mod.make_progression import make_arithmetic
from Brain_games.Games.mod.check import do_check


def do_game_progression():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        progression = make_arithmetic()
        index = randint(0, len(progression) - 1)
        right_answer = progression[index]
        progression[index] = '..'
        print('Question:', (' '.join(str(el) for el in progression)))
        answer = prompt.integer('Your answer: ')
        if do_check(answer, right_answer) == 'Correct':
            print(do_check(answer, right_answer))
            count += 1
        else:
            print(do_check(answer, right_answer), f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    do_game_progression()
