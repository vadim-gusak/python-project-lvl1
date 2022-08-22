from random import choice, randint


START = 1
END = 15
OPERATORS = ('+', '-', '*')


def corr_anser(first, second, operator):
    anser = 0
    if operator == '+':
        anser = first + second
    elif operator == '-':
        anser = first - second
    else:
        anser = first * second
    return anser


def main():
    random_first = randint(START, END)
    random_second = randint(START, END)
    random_operator = choice(OPERATORS)
    question = (f'{random_first} {random_operator} {random_second}')
    print(f'Question: {question}')
    correct_anser = corr_anser(random_first, random_second, random_operator)
    return correct_anser


def task():
    print('What is the result of the expression?')
