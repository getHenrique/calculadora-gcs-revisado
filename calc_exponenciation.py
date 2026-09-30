# calc_exponenciation
# Module B - Exponenciation and root extraction operations

SQUARE_ROOT_EXPONENT = 1 / 2
CUBE_ROOT_EXPONENT = 1 / 3


def to_power_of(base, exponent):
    """Returns the base to the power of the expoent."""
    return base ** exponent


def square_root_of(radicand):
    """Returns the square root of the radicand."""
    return radicand ** SQUARE_ROOT_EXPONENT


def cube_root_of(radicand):
    """Returns the cube root of the radicand."""
    return radicand ** CUBE_ROOT_EXPONENT


def exponenciation_menu():

    user_input = '0'
    
    while user_input != '4':
        user_input = input(    
            "1 - Potência\n"
            "2 - Raiz Quadrada\n"
            "3 - Raiz Cúbica\n"
            "4 - Cancelar operação\n"
            ">> "
        )
        match user_input:
            case '1':
                print("\nPotência de A^B")
                print(
                    "A^B = ",
                    to_power_of(
                        float(input("A = ")),
                        float(input("B = "))
                    ),
                    "\n"
                )
            case '2':
                print("\nRaiz quadrada de X")
                print(
                    "√X = ",
                    square_root_of(float(input("X = "))),
                    "\n"
                )
            case '3':
                print("\nRaiz cúbica de X")
                print(
                    "∛X = ",
                    cube_root_of(float(input("X = "))),
                    "\n"
                )
            case '4':
                print("Saindo do módulo...\n")
                break
            case _:
                print("Input inválido\n")