"""Module contains mathematical functions for games."""

from math import sqrt


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
    """Сheck if a number is even.

    Args:
        number (int): the number to check

    Returns:
        bool: the result of checking
    """
    num_parity_indicator = 2
    required_remainder = 0
    return number % num_parity_indicator == required_remainder


def is_remainder(divisor: int, number: int) -> bool:
    """Check if there is a remainder after dividing the number by the divisor.

    Args:
        divisor (int): divisor of the passed number
        number (int): number to be divided

    Returns:
        bool: the result of checking
    """
    no_remainder = 0
    return number % divisor != no_remainder


def is_prime(number: int) -> bool:
    """Check if a number is prime.

    Args:
        number (int): the number to check

    Returns:
        bool: the result of checking
    """
    min_even_prime = 2
    if is_even(number):
        return number == min_even_prime

    odd_divisor = 3
    while odd_divisor <= sqrt(number) and is_remainder(odd_divisor, number):
        odd_divisor += min_even_prime
    return odd_divisor > sqrt(number)
