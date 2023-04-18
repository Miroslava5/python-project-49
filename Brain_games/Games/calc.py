import prompt
from random import randint
from Brain_games.Games.check import do_check

def do_game_calc():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression? ')
    count = 0
    while count < 3:
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        symbols = ['+', '-', '*']
        index_symbols = randint(0,2)
        print(f'Question: {number1} {symbols[index_symbols]} {number2}')
        match symbols[index_symbols]:
            case '+':
                right_answer = number1 + number2
            case '-':
                right_answer = number1 - number2
            case '*':
                right_answer = number1 * number2
        answer = prompt.integer('Your answer: ')
        if do_check(answer, right_answer) == 'Correct':
            print(do_check(answer, right_answer))
            count += 1
        else:
            return print(do_check(answer, right_answer)+ f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')

if __name__ == '__main__':
    do_game_calc()
