import prompt
from random import randint


def do_game_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        number = randint(0, 1000)
        print('Question: ', number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            right_answer = 'yes'
            if answer == right_answer:
                print('Correct!')
                count += 1
            else:
                return print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\n Let's try again, {name}!")
        else:
            right_answer = 'no'
            if answer == right_answer:
                print('Correct!')
                count +=1
            else:
                return print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\n Let's try again, {name}!")
    print(f'Congratulations, {name}!')
    return


if __name__ == '__main__':
    do_game_even()
