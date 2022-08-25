from random import randint


START = 1
END = 100
DIFF_START = 1
DIFF_END = 100
LENGTH_START = 1
LENGTH_MIN = 5
LENGTH_END = 10
TASK = 'What number is missing in the progression?'


def calc_term(initial_term, common_difference, n):
    term = initial_term + (n - 1) * common_difference
    return term


def create_question(prog_length, start_term, difference, rand_num):
    index = 1
    question = ''
    while index <= prog_length:
        if index == rand_num:
            question = f'{question} ...'
        else:
            question = f'{question} {calc_term(start_term, difference, index)}'
        index += 1
    return question


def question_and_answer():
    initial_term = randint(START, END)
    difference = randint(DIFF_START, DIFF_END)
    prog_length = randint(LENGTH_MIN, LENGTH_END)
    rand_num = randint(LENGTH_START, prog_length)

    question = create_question(prog_length, initial_term, difference, rand_num)
    answer = calc_term(initial_term, difference, rand_num)
    return (question.strip(), str(answer))
