

def do_check(answer, right_answer):
    if answer == right_answer:
        check_text = 'Correct'
    else:
        check_text = f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\n"
    return check_text


if __name__ == '__main__':
    do_check()
