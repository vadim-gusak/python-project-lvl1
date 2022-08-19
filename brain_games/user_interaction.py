import prompt


CALC_GAME = 'brain_calc'
EVEN_GAME = 'even_game'
GCD_GAME = 'gcd_game'


def greeting():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def loss(user_anser, correct_anser, user_name):
    print(f"'{user_anser}' is wrong answer ;(. "
          f"Correct answer was '{correct_anser}'.")
    print(f"Let's try again, {user_name}!")


def win(user_name):
    print(f'Congratulations, {user_name}!')


def end(name, wrong_count, user_anser, correct_anser):
    if wrong_count == 0:
        win(name)
    else:
        loss(user_anser, correct_anser, name)


def task(game_num):
    if game_num == EVEN_GAME:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    if game_num == CALC_GAME:
        print('What is the result of the expression?')
    if game_num == GCD_GAME:
        print('Find the greatest common divisor of given numbers.')
