import prompt
from random import choice, randint
import brain_games.user_interaction


START = 1
END = 15
NUM_OF_ROUNDS = 3
OPERATORS = ('+', '-', '*')


def correct_anser_func(first, second, operator):
    anser = 0
    if operator == '+':
        anser = first + second
    elif operator == '-':
        anser = first - second
    else:
        anser = first * second
    return anser


def is_correct(user_anser, correct_anser):
    if user_anser == str(correct_anser):
        print('Correct!')
        return True
    return False


def brain_calc(name):

    wrong_count = 0
    correct_count = 0

    while wrong_count == 0 and correct_count < NUM_OF_ROUNDS:
        random_first = randint(START, END)
        random_second = randint(START, END)
        random_operator = choice(OPERATORS)
        question = (f'{random_first} {random_operator} {random_second}')
        print(f'Question: {question}')
        user_anser = prompt.string('Your answer: ')
        correct_anser = correct_anser_func(random_first, random_second, random_operator)
        if is_correct(user_anser, correct_anser):
            correct_count += 1
        else:
            wrong_count += 1


    if wrong_count == 0:
        brain_games.user_interaction.win(name)
    else:
        brain_games.user_interaction.loss(user_anser, correct_anser, name)

