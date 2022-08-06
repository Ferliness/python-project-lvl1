"""Module contains mathematical functions for games."""


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


def is_even(number: int) -> bool:
    """Сhecks if a number is even, return True/False.

    Args:
        number (int): the number to check

    Returns:
        bool: the result of checking
    """
    num_parity_indicator = 2
    required_remainder = 0
    return number % num_parity_indicator == required_remainder
