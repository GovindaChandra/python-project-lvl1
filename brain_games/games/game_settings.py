"""Global settings for games."""

import prompt

from brain_games.cli import welcome

NUMBER_OF_QUESTIONS = 3
GAME_OVER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
GAME_WIN = 'Congratulations, {0}!\n'


def game_engine(game_rule, game_function):
    """Call greeting, lunch game function.

    Parameters:
        game_rule: Describe game rules
        game_function: game logic function
    """
    name = welcome(game_rule)
    for step in range(NUMBER_OF_QUESTIONS):
        expression, correct_answer = game_function()
        print('Question:', expression)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            if step == NUMBER_OF_QUESTIONS - 1:
                print(GAME_WIN.format(name))
        else:
            print(GAME_OVER.format(answer, correct_answer))
            print("Let's try again, {0}!\n".format(name))
            break
