"""The module for the game brain-prog."""

from random import choice, randint
from typing import List

DESCRIPTION = 'What number is missing in the progression?'
MIN_NUM, MAX_NUM = 0, 100
REC_LEN_LIST, PART_OF_MAX = 10, 0.5


def get_question_and_answer() -> tuple[str, str]:
    """Generate and give a game question and answer to it.

    Returns:
        tuple[str, str]: (question, answer)
    """
    progression = gen_progression()
    hidden_element = choice(progression)

    question = 'Question: {hidden_progression}'.format(
        hidden_progression=' '.join(make_hidden_prog(
            progression,
            hidden_element,
        ),
        ),
    )
    answer = str(hidden_element)

    return question, answer


def make_hidden_prog(progression: List[int], element: int) -> List[str]:
    """Hide the accepted progression element.

    Args:
        progression (List[int]): some progression
        element (int): the element to hide

    Returns:
        List[str]: list of strings based on progression
        without one element
    """
    return [
        '..' if num == element else str(num)
        for num in progression
    ]


def gen_progression() -> List[int]:
    """Generate a progression of random numbers of lenght REC_LEN_LIST.

    MAX_NUM must be greater than: MAX_NUM * PART_OF_MAX + REC_LEN_LIST.

    Returns:
        List[int]: the random progression
    """
    max_fst_num = int(MAX_NUM * PART_OF_MAX)
    fst_num = randint(MIN_NUM, max_fst_num)

    min_last_num = fst_num + REC_LEN_LIST
    last_num = randint(min_last_num, MAX_NUM)

    step = int((last_num - fst_num) / REC_LEN_LIST)

    return list(range(fst_num, last_num, step))[:REC_LEN_LIST]
