from random import randint

START = 1
END = 10
MULTIPLE_MIN = 2
MULTIPLE_MAX = 10
TASK = 'Find the greatest common divisor of given numbers.'


def corr_answer(first, second):
    if second == 0:
        return first
    else:
        return corr_answer(second, first % second)


def question_and_answer():
    random_num = randint(START, END)
    random_mul_first = randint(MULTIPLE_MIN, MULTIPLE_MAX)
    random_mul_second = randint(MULTIPLE_MIN, MULTIPLE_MAX)
    first_num = random_num * random_mul_first
    second_num = random_num * random_mul_second
    question = f'{first_num} {second_num}'
    correct_answer = corr_answer(first_num, second_num)
    return (question, str(correct_answer))
