"""The module for the game brain-even."""

from random import randint
from typing import Tuple

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM, MAX_NUM = 0, 100


def get_question_and_answer() -> Tuple[str, str]:
    """Generate and give a game question and answer to it.

    Returns:
        Tuple[str, str]: (question, answer)
    """
    answer_dict = {True: 'yes', False: 'no'}
    number = randint(MIN_NUM, MAX_NUM)

    question = str(number)
    answer = answer_dict[is_even(number)]

    return question, answer


def is_even(number: int) -> bool:
    """Сheck if a number is even.

    Args:
        number (int): the number to check

    Returns:
        bool: the result of checking
    """
    return number % 2 == 0
