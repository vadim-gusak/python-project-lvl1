from random import randint


START = 1
END = 999


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def corr_anser(num):
    if is_even(num):
        return 'yes'
    return 'no'


def brain_even():

    random_num = randint(START, END)
    print(f'Question: {random_num}')
    correct_anser = corr_anser(random_num)
    return correct_anser
