import prompt


NUM_OF_ROUNDS = 3


def game(game_module):
    user_name = greeting()
    game_module.task()
    wrong = 0
    win = 0
    while wrong == 0 and win < NUM_OF_ROUNDS:
        correct_anser = str(game_module.main())
        user_anser = prompt.string('Your answer: ')
        if user_anser == correct_anser:
            win += 1
            print('Correct!')
        else:
            wrong += 1
    end(user_name, wrong, user_anser, correct_anser)


def greeting():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def end(user_name, wrong_count, user_anser, correct_anser):
    if wrong_count == 0:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"'{user_anser}' is wrong answer ;(. "
              f"Correct answer was '{correct_anser}'.")
        print(f"Let's try again, {user_name}!")
