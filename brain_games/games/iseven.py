"""Is even? - game logic."""

import secrets

GAME_RULE = 'Answer "yes" if number is even, otherwise answer "no".\n'


def game_data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
    secrets_generator = secrets.SystemRandom()
    number = secrets_generator.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
