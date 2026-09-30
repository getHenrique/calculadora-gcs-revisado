# calc_basics
# Module A - Basic Operations


def add(addend_a, addend_b):
    """Returns the sum of addend a and addend b."""


    return addend_a + addend_b


def subtract(minuend, subtrahend):
    """Returns the difference between the minuend and the subtrahend."""


    return minuend - subtrahend


def multiply(factor_a, factor_b):
    """Returns the product of factor a and factor b."""


    return factor_a * factor_b


def divide(dividend, divisor):
    """
    Returns the quocient of the division between the dividend and the divisor.
    Throws ZeroDivisionError if the divisor is 0.
    """


    try:
        return dividend / divisor
    except ZeroDivisionError:
        print("É impossível dividir por zero.")