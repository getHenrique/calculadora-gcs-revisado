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


def basics_menu():


    user_input = '0'

    while user_input != '5':
        user_input = input(    
            "1 - Somar\n",
            "2 - Subtrair\n",
            "3 - Multiplicar\n",
            "4 - Dividir\n",
            "5 - Cancelar operação\n",
            ">> "
        )
        match user_input:
            case '1':
                print("\nSomando A + B")
                print(
                    "A + B = ",
                    add(
                        float(input("A = ")),
                        float(input("B = "))
                    ),
                    "\n"
                )
            case '2':
                print("\nSubtraindo A - B")
                print(
                    "A - B = ",
                    subtract(
                        float(input("A = ")),
                        float(input("B = "))
                    ),
                    "\n"
                )
            case '3':
                print("\nMultiplicando A * B")
                print(
                    "A * B = ",
                    multiply(
                        float(input("A = ")),
                        float(input("B = "))
                    ),
                    "\n"
                )
            case '4':
                print("\nDividindo A / B")
                print(
                    "A / B = ",
                    divide(
                        float(input("A = ")),
                        float(input("B = "))
                    ),
                    "\n"
                )
            case '5':
                print("Saindo do módulo...\n")
                break
            case _:
                print("Input inválido\n")