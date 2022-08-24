from random import randint


START = 1
END = 999
TASK = 'Answer "yes" if the number is even, otherwise answer "no"'


def main():
    question = randint(START, END)
    correct_anser = 'no'
    if question % 2 == 0:
        correct_anser = 'yes'
    return (question, correct_anser)
