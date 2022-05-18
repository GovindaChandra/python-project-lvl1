"""Expression calculation game logic."""

import secrets

from brain_games.game_engine.game_engine import start_game

GAME_RULE = 'What is the result of the expression?\n'


def _calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def _game_data_generation():
    secrets_generator = secrets.SystemRandom()
    num1 = secrets_generator.randint(1, 100)
    num2 = secrets_generator.randint(1, 100)
    operator = secrets_generator.choice(('+', '-', '*'))
    correct_answer = _calc(num1, num2, operator)
    return '{0} {1} {2}'.format(num1, operator, num2), str(correct_answer)


def brain_calc():
    """Start the brain-calc game."""
    start_game(GAME_RULE, _game_data_generation)
