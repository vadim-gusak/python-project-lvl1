from random import randint


START = 1
END = 999
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def question_and_answer():
    question = randint(START, END)
    correct_answer = 'no'
    if is_even(question):
        correct_answer = 'yes'
    return question, correct_answer
