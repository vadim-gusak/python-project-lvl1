import prompt
from random import randint


START = 1
END = 999
NUM_OF_ROUNDS = 3


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def greeting():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return user_name


def brain_even():
    name = greeting()

    wrong_count = 0
    correct_count = 0
    correct_anser = ''

    while wrong_count == 0 and correct_count < NUM_OF_ROUNDS:
        random_num = randint(START, END)
        print(f'Question: {random_num}')
        user_anser = prompt.string('Your answer: ')
        if (is_even(random_num) and user_anser == 'yes'):
            print('Correct!')
            correct_count += 1
        elif not is_even(random_num) and user_anser == 'no':
            print('Correct!')
            correct_count += 1
        else:
            if is_even(random_num):
                correct_anser = 'yes'
            else:
                correct_anser = 'no'
            print(f"'{user_anser}' is wrong answer ;(. "
                  f"Correct answer was '{correct_anser}'.")
            print(f"Let's try again, {name}!")
            wrong_count += 1

    if wrong_count == 0:
        print(f'Congratulations, {name}!')
