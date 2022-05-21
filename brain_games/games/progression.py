"""Arithmetic progression game logic."""

import secrets

GAME_RULE = 'What number is missing in the progression?\n'


def game_data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
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
