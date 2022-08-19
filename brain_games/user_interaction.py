import prompt


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
