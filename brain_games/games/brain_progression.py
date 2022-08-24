from random import randint


START = 1
END = 100
DIFF_START = 1
DIFF_END = 100
LENGTH_START = 5
LENGTH_END = 10
TASK = 'What number is missing in the progression?'


def main():
    sum = randint(START, END)
    add_num = randint(DIFF_START, DIFF_END)
    prog_length = randint(LENGTH_START, LENGTH_END)
    rand_num = randint(LENGTH_START, prog_length)
    index = 1
    question = ''
    anser = ''
    while index <= prog_length:
        if index != rand_num:
            question = question + str(sum) + ' '
            sum = sum + add_num
        else:
            question = question + '... '
            anser = sum
            sum = sum + add_num
        index += 1
    return (question.strip(), str(anser))
