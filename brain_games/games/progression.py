"""Arithmetic progression game logic."""

import random

GAME_RULE = 'What number is missing in the progression?\n'


def _progression_generation():
    members_count = random.randint(5, 10)
    first_num = random.randint(1, 100)
    diff = random.randint(-members_count, members_count)
    progression = []
    for _ in range(members_count):
        progression.append(first_num)
        first_num += diff
    return progression


def game_data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
    progression = _progression_generation()
    index = random.randint(0, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'
    return ' '.join(map(str, progression)), str(correct_answer)
