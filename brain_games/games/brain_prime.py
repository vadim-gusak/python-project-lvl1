from random import randint


START = 1
END = 100


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
    num = randint(START, END)
    print(f'Question: {num}')
    anser = ''
    if is_prime(num):
        anser = 'yes'
    else:
        anser = 'no'
    return anser


def task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
