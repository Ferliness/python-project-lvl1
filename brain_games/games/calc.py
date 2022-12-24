"""The module for the game brain-calc."""

import operator
from random import choice, randint
from typing import Tuple

DESCRIPTION = 'What is the result of the expression?'
MIN_NUM, MAX_NUM = 0, 100


def get_question_and_answer() -> Tuple[str, str]:
    """Generate and give a game question and answer to it.

    Returns:
        Tuple[str, str]: (question, answer)
    """
    first_num, second_num = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)
    operation_name, operation_method = choice((
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    ),
    )

    question = f'{first_num} {operation_name} {second_num}'
    answer = str(operation_method(first_num, second_num))

    return question, answer
