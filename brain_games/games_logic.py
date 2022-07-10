"""Module contains functions with the main logic of games."""

import prompt


def print_start_phrase():
    """Greet the player with a common phrase."""
    print('Welcome to the Brain Games!')


def meet_and_greet_player():
    """Ask and get the player's name and print the greeting.

    Returns:
        string: the player's name
    """
    player_name = prompt.string(prompt='May I have your name? ')
    print('Hello,', player_name)
    return player_name


def get_player_answer():
    """Asks the player for an answer and returns it.

    Returns:
        string: thr player's answer
    """
    return prompt.string(prompt='Your answer: ')


def compare_answers(correct_answer, player_answer):
    """Compare the player's answer with the correct one.

    Print the comparison result and then return it.

    Args:
        correct_answer (string): the correct answer to the question
        player_answer (string): the player answer to the question

    Returns:
        bool: if the player right return True, else False
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


def print_end_phrase(is_player_wins, player_name):
    """Print the appropriate finish phrase.

    Args:
        is_player_wins (bool): is the player a winner or a loser
        player_name (string): the player's name
    """
    if is_player_wins:
        print('Congratulations,', player_name)
    else:
        print("Let's try again,", player_name)
