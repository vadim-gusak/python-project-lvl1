import prompt
from random import randint
import brain_games.user_interaction


START = 1
END = 999
NUM_OF_ROUNDS = 3
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
user_anser = ''
correct_anser = ''


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


def correct_anser_func(num):
    if is_even(num):
        return 'yes'
    return 'no'


def brain_even():
    name = brain_games.user_interaction.greeting(TASK)

    wrong_count = 0
    correct_count = 0
    correct_anser = ''

    while wrong_count == 0 and correct_count < NUM_OF_ROUNDS:
        random_num = randint(START, END)
        print(f'Question: {random_num}')
        user_anser = prompt.string('Your answer: ')
        if is_correct(user_anser, random_num):
            correct_count += 1
        else:
            wrong_count += 1
            correct_anser = correct_anser_func(random_num)

    if wrong_count == 0:
        brain_games.user_interaction.win(name)
    else:
        brain_games.user_interaction.loss(user_anser, correct_anser, name)
