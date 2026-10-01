# calc_statistisc
# Module D - Statistics operations

from calc_exponenciation import square_root_of
from value_inputs import get_number_set


def average(number_set: list[float]) -> float:
    """Returns the average of a set of values."""
    if not number_set:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        return sum(number_set) / len(number_set)


def median(number_set: list[float]) -> float:
    """Returns the median of a set of values."""
    if not number_set:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        sorted_number_set = sorted(number_set)
        number_set_size = len(sorted_number_set)
        if (number_set_size % 2) == 0:
            return (
                sorted_number_set[(number_set_size // 2) - 1]
                + sorted_number_set[number_set_size // 2]
            ) / 2
        else:
            return sorted_number_set[number_set_size // 2]


def standard_deviation(number_set: list[float]) -> float:
    """Returns the standard deviation of a set of values."""
    if not number_set:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        return square_root_of(
            sum(
                ((value - average(number_set)) ** 2) for value in number_set
            ) / len(number_set)
        )


def statistics_menu():

    user_input: str = '0'
    number_set: list[float]

    while user_input != '4':
        user_input = input(    
            "1 - Média\n"
            "2 - Mediana\n"
            "3 - Desvio Padrão\n"
            "4 - Cancelar operação\n"
            ">> "
        )
        match user_input:
            case '1':
                print("\nMédia de um conjunto de números")
                number_set = get_number_set()
                print(
                    "Média de ",
                    number_set,
                    " = ",
                    average(number_set),
                    "\n"
                )
            case '2':
                print("\nMediana de um conjunto de números")
                number_set = get_number_set()
                print(
                    "Mediana de ",
                    number_set,
                    " = ",
                    median(number_set),
                    "\n"
                )
            case '3':
                print("\nDesvio padrão populacional de um conjunto de números")
                number_set = get_number_set()
                print(
                    "Desvio Padrão populacional de ",
                    number_set,
                    " = ",
                    standard_deviation(number_set),
                    "\n"
                )
            case '4':
                print("Saindo do módulo...\n")
                break
            case _:
                print("Entrada inválida!\n")