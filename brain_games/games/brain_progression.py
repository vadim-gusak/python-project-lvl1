from random import randint


START = 1
END = 100
DIFF_START = 1
DIFF_END = 100
LENGTH_START = 1
LENGTH_MIN = 5
LENGTH_END = 10
TASK = 'What number is missing in the progression?'


def calc_term(initial_term, difference, n):
    term = initial_term + (n - 1) * difference
    return term


def create_question(progression, rand_num):
    progression[rand_num - 1] = '..'
    question = " ".join(progression)
    return question


def create_progression(prog_lengh, initial_term, difference):
    index = 1
    progression = []
    while index <= prog_lengh:
        elem = str(calc_term(initial_term, difference, index))
        progression.append(elem)
        index += 1
    return progression


def question_and_answer():
    initial_term = randint(START, END)
    difference = randint(DIFF_START, DIFF_END)
    prog_length = randint(LENGTH_MIN, LENGTH_END)
    rand_num = randint(LENGTH_START, prog_length)
    progression = create_progression(prog_length, initial_term, difference)
    question = create_question(progression, rand_num)
    answer = calc_term(initial_term, difference, rand_num)
    return question, str(answer)
