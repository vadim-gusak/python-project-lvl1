import prompt
from random import randint
from brain_games.user_interaction import end

START = 1
END = 10
MULTIPLE_MIN = 2
MULTIPLE_MAX = 10
NUM_OF_ROUNDS = 3


def corr_anser(first, second):
    if second == 0:
        return first
    else:
        return corr_anser(second, first % second)


def is_correct(user_anser, correct_anser):
    if user_anser == str(correct_anser):
        print('Correct!')
        return True
    return False


def brain_gcd(name):
    wrong_count = 0
    correct_count = 0

    while wrong_count == 0 and correct_count < NUM_OF_ROUNDS:
        random_num = randint(START, END)
        random_mul_first = randint(MULTIPLE_MIN, MULTIPLE_MAX)
        random_mul_second = randint(MULTIPLE_MIN, MULTIPLE_MAX)
        first_num = random_num * random_mul_first
        second_num = random_num * random_mul_second
        print(f'Question: {first_num} {second_num}')
        user_anser = prompt.string('Your answer: ')
        correct_anser = corr_anser(first_num, second_num)
        if is_correct(user_anser, correct_anser):
            correct_count += 1
        else:
            wrong_count += 1

    end(name, wrong_count, user_anser, correct_anser)
