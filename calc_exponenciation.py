# calc_exponenciation
# Module B - Exponenciation and root extraction operations

from value_inputs import get_single_float, get_two_floats

SQUARE_ROOT_EXPONENT: float = 1 / 2
CUBE_ROOT_EXPONENT: float = 1 / 3


def to_power_of(base: float, exponent: float) -> float:
    """Returns the base to the power of the expoent."""
    return base ** exponent


def square_root_of(radicand: float) -> float:
    """Returns the square root of the radicand."""
    return radicand ** SQUARE_ROOT_EXPONENT


def cube_root_of(radicand: float) -> float:
    """Returns the cube root of the radicand."""
    return radicand ** CUBE_ROOT_EXPONENT


def exponenciation_menu():

    user_input: str = '0'
    value_input_a: float
    value_input_b: float
    value_input_x: float
    
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
                value_input_a, value_input_b = get_two_floats()
                print(
                    "A^B = ",
                    to_power_of(
                        value_input_a,
                        value_input_b
                    ),
                    "\n"
                )
            case '2':
                print("\nRaiz quadrada de X")
                value_input_x = get_single_float()
                print(
                    "√X = ",
                    square_root_of(value_input_x),
                    "\n"
                )
            case '3':
                print("\nRaiz cúbica de X")
                value_input_x = get_single_float()
                print(
                    "∛X = ",
                    cube_root_of(value_input_x),
                    "\n"
                )
            case '4':
                print("Saindo do módulo...\n")
                break
            case _:
                print("Entrada inválida!\n")