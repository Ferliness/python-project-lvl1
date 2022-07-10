"""Module contains all generator functions used in games."""

from random import randrange

MIN_NUM, MAX_NUM, GAMES_COUNT = 0, 100, 3


def gen_number():
    """Give a number in the range from the MIN_NUM to the MAX_NUM.

    Returns:
        int: the random number
    """
    return randrange(MIN_NUM, MAX_NUM)


def gen_nums_list():
    """Give a list of numbers of length the GAMES_COUNT.

    Returns:
        list: the list of random numbers
    """
    return [gen_number() for _ in range(GAMES_COUNT)]


def gen_tuples_list():
    """Generate a list of random numbers in tuples.

    Returns:
        list: the list of tuples
    """
    return list(zip(gen_nums_list(), gen_nums_list()))


def gen_math_operator():
    """Give a math operator from the tuple of operators.

    Returns:
        string: the math operator
    """
    tuple_operators = ('+', '-', '*')
    return tuple_operators[randrange(len(tuple_operators))]
