"""Global settings for games."""

import prompt
from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3
GAME_OVER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def start_game(game_rule, game_function):
    """Call greeting, lunch game function.

    Parameters:
        game_rule: Describe game rules
        game_function: game logic function
    """
    name = welcome_user()
    print(game_rule)
    for _ in range(NUMBER_OF_ROUNDS):
        expression, correct_answer = game_function()
        print('Question:', expression)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(GAME_OVER.format(answer, correct_answer))
            print("Let's try again, {0}!\n".format(name))
            break
        print('Correct!')
    else:
        print('Congratulations, {0}!\n'.format(name))
