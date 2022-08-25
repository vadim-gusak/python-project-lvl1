import prompt


NUM_OF_ROUNDS = 3


def play_game(game_module):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.TASK)

    win = 0
    while win < NUM_OF_ROUNDS:
        (question, correct_answer) = game_module.question_and_answer()
        print(f'Question: {question}')
        user_anser = prompt.string('Your answer: ')
        if user_anser == correct_answer:
            win += 1
            print('Correct!')
        else:
            print(f"'{user_anser}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
