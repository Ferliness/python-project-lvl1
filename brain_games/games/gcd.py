"""The module for the game brain-gcd."""

from math import gcd
from random import randint
from typing import Tuple

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUM, MAX_NUM = 0, 100


def get_question_and_answer() -> Tuple[str, str]:
    """Generate and give a game question and answer to it.

    Returns:
        Tuple[str, str]: (question, answer)
    """
    first_num, second_num = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)

    question = f'{first_num} {second_num}'
    answer = str(gcd(first_num, second_num))

    return question, answer
