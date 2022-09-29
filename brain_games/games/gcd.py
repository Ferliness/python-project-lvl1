"""The module for the game brain-gcd."""

from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUM, MAX_NUM = 0, 100


def get_question_and_answer() -> tuple[str, str]:
    """Generate and give a game question and answer to it.

    Returns:
        tuple[str, str]: (question, answer)
    """
    fst_num, snd_num = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)

    question = f'Question: {fst_num} {snd_num}'
    answer = str(gcd(fst_num, snd_num))

    return question, answer
