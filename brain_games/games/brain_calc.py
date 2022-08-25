from random import choice, randint


START = 1
END = 15
OPERATORS = ('+', '-', '*')
TASK = 'What is the result of the expression?'


def question_and_answer():
    random_first = randint(START, END)
    random_second = randint(START, END)
    random_operator = choice(OPERATORS)
    question = (f'{random_first} {random_operator} {random_second}')
    correct_answer = 0
    if random_operator == '+':
        correct_answer = random_first + random_second
    elif random_operator == '-':
        correct_answer = random_first - random_second
    else:
        correct_answer = random_first * random_second
    return (question, str(correct_answer))
