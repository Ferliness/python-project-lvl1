"""The module for the game brain-calc."""

from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
MIN_NUM, MAX_NUM = 0, 100


def get_question_and_answer() -> tuple[str, str]:
    """Generate and give a game question and answer to it.

    Returns:
        tuple[str, str]: (question, answer)
    """
    fst_num, snd_num = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)
    math_operator = gen_math_operator()

    question = f'Question: {fst_num} {math_operator} {snd_num}'
    answer = str(calc_expression(fst_num, snd_num, math_operator))

    return question, answer


def gen_math_operator() -> str:
    """Give a math operator from the tuple of operators.

    Returns:
        str: the math operator
    """
    tuple_operators = ('+', '-', '*')
    return choice(tuple_operators)


def calc_expression(
    fst_number: int,
    snd_number: int,
    math_operator: str,
) -> int:
    """Calculate an expression and return the result, only '+', '-', '*'.

    Args:
        fst_number (int): first coefficent
        snd_number (int): second coefficent
        math_operator (str): type of operation

    Returns:
        int: expression result
    """
    if math_operator == '+':
        return fst_number + snd_number
    elif math_operator == '-':
        return fst_number - snd_number

    return fst_number * snd_number
