"""Module contains all generator functions used in games."""

from random import randint, randrange
from typing import Any, Callable, List

MIN_NUM, MAX_NUM, GAMES_COUNT = 0, 100, 3
REC_LEN_LIST, PART_OF_MAX = 10, 0.5


def gen_gm_list(gen_smth: Callable[..., Any]) -> List[Any]:
    """Give a game list of length GAMES_COUNT.

    Args:
        gen_smth (Callable[..., Any]): a generator function

    Returns:
        list: list of random values
    """
    return [gen_smth() for _ in range(GAMES_COUNT)]


def gen_number(min_num: int = MIN_NUM, max_num: int = MAX_NUM) -> int:
    """Give a number in the range from the min_num to the max_num.

    Default MIN_NUM and MAX_NUM,
    the min_num and max_num must be greater than zero
    and min_num must be less than the max_num.
    Minimum and maximum are included in the bounds.

    Args:
        min_num (int): the minimum allowed number
        max_num (int): the maximum allowed number

    Returns:
        int: the random number
    """
    return randint(min_num, max_num)


def gen_num_tuple() -> tuple:
    """Generate a tuple of random numbers.

    Returns:
        tuple: tuple with numbers
    """
    return (gen_number(), gen_number())


def gen_math_operator() -> str:
    """Give a math operator from the tuple of operators.

    Returns:
        str: the math operator
    """
    tuple_operators = ('+', '-', '*')
    return tuple_operators[randrange(len(tuple_operators))]


def gen_prog() -> List[int]:
    """Generate a progression of random numbers of lenght REC_LEN_LIST.

    MAX_NUM must be greater than: MAX_NUM * PART_OF_MAX + REC_LEN_LIST.

    Returns:
        List[int]: the random progression
    """
    fst_num = gen_number(MIN_NUM, int(MAX_NUM * PART_OF_MAX))
    last_num = gen_number(fst_num + REC_LEN_LIST, MAX_NUM)
    step = int((last_num - fst_num) / REC_LEN_LIST)
    return list(range(fst_num, last_num, step))[:REC_LEN_LIST]
