from random import randint

START = 1
END = 10
MULTIPLE_MIN = 2
MULTIPLE_MAX = 10


def corr_anser(first, second):
    if second == 0:
        return first
    else:
        return corr_anser(second, first % second)


def brain_gcd():

    random_num = randint(START, END)
    random_mul_first = randint(MULTIPLE_MIN, MULTIPLE_MAX)
    random_mul_second = randint(MULTIPLE_MIN, MULTIPLE_MAX)
    first_num = random_num * random_mul_first
    second_num = random_num * random_mul_second
    print(f'Question: {first_num} {second_num}')
    correct_anser = corr_anser(first_num, second_num)
    return correct_anser
