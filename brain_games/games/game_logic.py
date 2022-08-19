import brain_games.user_interaction
import brain_games.games.brain_even
import brain_games.games.brain_calc
import brain_games.games.brain_gcd
import prompt


CALC_GAME = 'brain_calc'
EVEN_GAME = 'even_game'
GCD_GAME = 'gcd_game'


NUM_OF_ROUNDS = 3


def play(game_num):
    anser = 0
    if game_num == EVEN_GAME:
        anser = brain_games.games.brain_even.brain_even()
    if game_num == CALC_GAME:
        anser = brain_games.games.brain_calc.brain_calc()
    if game_num == GCD_GAME:
        anser = brain_games.games.brain_gcd.brain_gcd()
    return anser


def game(game_num):
    name = brain_games.user_interaction.greeting()
    brain_games.user_interaction.task(game_num)
    wrong = 0
    win = 0
    while wrong == 0 and win < NUM_OF_ROUNDS:
        correct_anser = str(play(game_num))
        user_anser = prompt.string('Your answer: ')
        if user_anser == correct_anser:
            win += 1
            print('Correct!')
        else:
            wrong += 1

    brain_games.user_interaction.end(name, wrong, user_anser, correct_anser)
