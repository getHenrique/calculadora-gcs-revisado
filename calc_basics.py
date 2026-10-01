# calc_basics
# Module A - Basic Operations

from value_inputs import get_two_floats


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
    if divisor == 0:
        raise ValueError("É impossível dividir por zero.")
    return dividend / divisor


def basics_menu():

    user_input = '0'
    value_input_a: float
    value_input_b: float

    while user_input != '5':
        user_input = input(    
            "1 - Somar\n"
            "2 - Subtrair\n"
            "3 - Multiplicar\n"
            "4 - Dividir\n"
            "5 - Cancelar operação\n"
            ">> "
        )
        match user_input:
            case '1':
                print("\nSomando A + B")
                value_input_a, value_input_b = get_two_floats()
                print(
                    "A + B = ",
                    add(
                        value_input_a,
                        value_input_b
                    ),
                    "\n"
                )
            case '2':
                print("\nSubtraindo A - B")
                value_input_a, value_input_b = get_two_floats()
                print(
                    "A - B = ",
                    subtract(
                        value_input_a,
                        value_input_b
                    ),
                    "\n"
                )
            case '3':
                print("\nMultiplicando A * B")
                value_input_a, value_input_b = get_two_floats()
                print(
                    "A * B = ",
                    multiply(
                        value_input_a,
                        value_input_b
                    ),
                    "\n"
                )
            case '4':
                print("\nDividindo A / B")
                value_input_a, value_input_b = get_two_floats()
                print(
                    "A / B = ",
                    divide(
                        value_input_a,
                        value_input_b
                    ),
                    "\n"
                )
            case '5':
                print("Saindo do módulo...\n")
                break
            case _:
                print("Entrada inválida!\n")