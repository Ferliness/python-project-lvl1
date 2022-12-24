"""The module for the game brain-prog."""

from random import randint, randrange
from typing import List, Tuple

DESCRIPTION = 'What number is missing in the progression?'
MIN_NUM, MAX_NUM = 0, 100
LENGTH = 10


def get_question_and_answer() -> Tuple[str, str]:
    """Generate and give a game question and answer to it.

    Returns:
        Tuple[str, str]: (question, answer)
    """
    progression = generate_progression()
    hidden_index = randrange(0, LENGTH)
    answer, progression[hidden_index] = progression[hidden_index], '..'

    question = ' '.join(progression)

    return question, answer


def generate_progression() -> List[str]:
    """Generate a progression of random numbers.

    Returns:
        List[str]: the random progression
    """
    start = randint(MIN_NUM, MAX_NUM)
    step = randint(MIN_NUM, MAX_NUM)
    end = start + LENGTH * step

    return list(map(str, list(range(start, end, step))))
