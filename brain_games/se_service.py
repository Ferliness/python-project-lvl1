"""Module contains service functions with side effects common to games."""

from random import randint

import prompt

MIN_NUM, MAX_NUM = 0, 1000


def greet_player(player_name):
    """Greet the player with two phrases and their name.

    Args:
        player_name (string): the player's name to greet him
    """
    print('Welcome to the Brain Games!')
    print('Hello,', player_name)


def get_player_name():
    """Ask the player's name.

    Returns:
        string: player name
    """
    return prompt.string(prompt='May I have your name? ')


def generate_number():
    """Give number for games.

    Returns:
        int: required number in the range from MIN_NUM to MAX_NUM
    """
    return randint(MIN_NUM, MAX_NUM)


def get_player_answer():
    """Asks the player for an answer and returns it.

    Returns:
        string: player answer
    """
    return prompt.string(prompt='Your answer: ')


def compare_answers(correct_answer, player_answer):
    """Compare the player's answer with the correct one.

    Return and print compare result.

    Args:
        correct_answer (string): correct answer to the question
        player_answer (string): player answer to the question

    Returns:
        bool: if player right return True, else False
    """
    if player_answer == correct_answer:
        print('Correct!')
        return True

    print(
        "'",
        player_answer,
        "' is wrong answer ;(. Correct answer was '",
        correct_answer,
        "'",
        sep='',
    )
    return False


def print_end_phrases(is_player_wins, player_name):
    """Print the appropriate finish phrases.

    Args:
        is_player_wins (bool): is player a winner or a loser
        player_name (string): player name
    """
    if is_player_wins:
        print('Congratulations,', player_name)
    else:
        print("Let's try again,", player_name)
