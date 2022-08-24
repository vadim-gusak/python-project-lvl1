import prompt


NUM_OF_ROUNDS = 3


def game(game_module):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.TASK)

    wrong = 0
    win = 0
    while wrong == 0 and win < NUM_OF_ROUNDS:
        (question, correct_anser) = game_module.main()
        print(f'Question: {question}')
        user_anser = prompt.string('Your answer: ')
        if user_anser == correct_anser:
            win += 1
            print('Correct!')
        else:
            wrong += 1

    if wrong == 0:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"'{user_anser}' is wrong answer ;(. "
              f"Correct answer was '{correct_anser}'.")
        print(f"Let's try again, {user_name}!")
