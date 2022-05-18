"""Is even? - game logic."""

import secrets

from brain_games.game_engine.game_engine import start_game

GAME_RULE = 'Answer "yes" if number is even, otherwise answer "no".\n'


def _game_data_generation():
    secrets_generator = secrets.SystemRandom()
    number = secrets_generator.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer


def brain_even():
    """Start the brain-even game."""
    start_game(GAME_RULE, _game_data_generation)
