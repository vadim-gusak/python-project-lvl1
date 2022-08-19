import prompt
from random import randint
from brain_games.user_interaction import end


START = 1
END = 999
NUM_OF_ROUNDS = 3


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def is_correct(user_anser, num):
    if is_even(num) and user_anser == 'yes':
        print('Correct!')
        return True
    elif not is_even(num) and user_anser == 'no':
        print('Correct!')
        return True

    return False


def corr_anser(num):
    if is_even(num):
        return 'yes'
    return 'no'


def brain_even(name):

    wrong_count = 0
    correct_count = 0

    while wrong_count == 0 and correct_count < NUM_OF_ROUNDS:
        random_num = randint(START, END)
        print(f'Question: {random_num}')
        user_anser = prompt.string('Your answer: ')
        correct_anser = corr_anser(random_num)
        if is_correct(user_anser, random_num):
            correct_count += 1
        else:
            wrong_count += 1

    end(name, wrong_count, user_anser, correct_anser)
