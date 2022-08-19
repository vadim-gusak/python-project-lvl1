import brain_games.user_interaction
import brain_games.games.brain_even
import brain_games.games.brain_calc
import brain_games.games.brain_gcd


CALC_GAME = 'brain_calc'
EVEN_GAME = 'even_game'
GCD_GAME = 'gcd_game'


def game(game_num):
    name = brain_games.user_interaction.greeting()

    if game_num == EVEN_GAME:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        brain_games.games.brain_even.brain_even(name)
    if game_num == CALC_GAME:
        print('What is the result of the expression?')
        brain_games.games.brain_calc.brain_calc(name)
    if game_num == GCD_GAME:
        print('Find the greatest common divisor of given numbers.')
        brain_games.games.brain_gcd.brain_gcd(name)
