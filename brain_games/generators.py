"""Module contains all generator functions used in games."""

from random import randrange
from typing import Any, Callable

MIN_NUM, MAX_NUM, GAMES_COUNT = 0, 100, 3


def gen_gm_list(gen_smth: Callable[..., Any]) -> list:
    """Give a game list of length GAMES_COUNT.

    Args:
        gen_smth (Callable[..., Any]): the generator function

    Returns:
        list: the list of random value
    """
    return [gen_smth() for _ in range(GAMES_COUNT)]


def gen_number() -> int:
    """Give a number in the range from the MIN_NUM to the MAX_NUM.

    Returns:
        int: the random number
    """
    return randrange(MIN_NUM, MAX_NUM)


def gen_num_tuple() -> tuple:
    """Generate a tuple of random numbers.

    Returns:
        tuple: the tuple with numbers
    """
    return (gen_number(), gen_number())


def gen_math_operator() -> str:
    """Give a math operator from the tuple of operators.

    Returns:
        str: the math operator
    """
    tuple_operators = ('+', '-', '*')
    return tuple_operators[randrange(len(tuple_operators))]
