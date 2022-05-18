"""Arithmetic progression game logic."""

import secrets

from brain_games.game_engine.game_engine import start_game

GAME_RULE = 'What number is missing in the progression?\n'


def _game_data_generation():
    count = secrets.SystemRandom().randint(5, 10)
    first_num = secrets.SystemRandom().randint(1, 100)
    diff = secrets.SystemRandom().randint(-count, count)
    progression = []
    if diff == 0:
        for _ in range(count):
            progression.append(first_num)
    else:
        progression = list(range(first_num, first_num + count * diff, diff))
    correct_answer = progression[abs(diff) - 1]
    progression[abs(diff) - 1] = '..'
    return ' '.join(map(str, progression)), str(correct_answer)


def brain_progression():
    """Start the brain-gcd game."""
    start_game(GAME_RULE, _game_data_generation)
