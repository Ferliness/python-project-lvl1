"""The module contains the main engine for brain games."""

from typing import Callable

import prompt

GAMES_COUNT = 3


def run_game(game: Callable[..., tuple[str, str]]) -> None:
    """Start the game.

    Args:
        game (Callable[..., tuple[str, str]): one of the brain games
    """
    print_start_phrase()
    player_name = meet_and_greet_player()
    print(game.DESCRIPTION)

    for _ in range(GAMES_COUNT):
        question, answer = game.get_question_and_answer()
        print(question)

        is_player_won = compare_answers(
            answer,
            get_player_answer(),
        )

        if is_player_won:
            continue

        break

    print_end_phrase(is_player_won, player_name)


def print_start_phrase() -> None:
    """Greet the player with a common phrase."""
    print('Welcome to the Brain Games!')


def meet_and_greet_player() -> str:
    """Ask and get the player's name and print the greeting.

    Returns:
        str: the player's name
    """
    player_name = prompt.string(prompt='May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def get_player_answer() -> str:
    """Asks the player for an answer and returns it.

    Returns:
        str: thr player's answer
    """
    return prompt.string(prompt='Your answer: ')


def compare_answers(correct_answer: str, player_answer: str) -> bool:
    """Compare the player's answer with the correct one.

    Print the comparison result and then return it.

    Args:
        correct_answer (str): the correct answer to the question
        player_answer (str): the player answer to the question

    Returns:
        bool: if the player right return True, else False
    """
    if player_answer == correct_answer:
        print('Correct!')
        return True

    print(
        f"'{player_answer}' is wrong answer ;(.",
        f"Correct answer was '{correct_answer}'.",
    )

    return False


def print_end_phrase(is_player_won: bool, player_name: str) -> None:
    """Print the appropriate finish phrase.

    Args:
        is_player_won (bool): is the player a winner or a loser
        player_name (str): the player's name
    """
    if is_player_won:
        print('Congratulations, ', player_name, '!', sep='')
    else:
        print("Let's try again, ", player_name, '!', sep='')
