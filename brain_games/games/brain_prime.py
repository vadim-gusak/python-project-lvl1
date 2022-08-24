from random import randint


START = 1
END = 100
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 1:
        return False
    index = 2
    while index <= num - 1:
        if num % index == 0:
            return False
        index += 1
    return True


def main():
    question = randint(START, END)
    anser = 'no'
    if is_prime(question):
        anser = 'yes'
    return (question, anser)
