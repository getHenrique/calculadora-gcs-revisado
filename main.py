# main menu

from calc_basics import basics_menu
from calc_conversion import conversion_menu
from calc_exponenciation import exponenciation_menu
from calc_percentage import percentage_menu
from calc_statistics import statistics_menu


def main_menu():

    user_input: str = '0'

    print("\n=== Calculadora GCS ===\n")
    while user_input != 'x':
        user_input = input(
            "a - Básico\n"
            "b - Potência\n"
            "c - Percentual\n"
            "d - Estatística\n"
            "e - Conversão\n"
            "x - Sair\n"
            ">> "
        )
        match user_input:
            case 'a':
                basics_menu()
            case 'b':
                exponenciation_menu()
            case 'c':
                percentage_menu()
            case 'd':
                statistics_menu()
            case 'e':
                conversion_menu()
            case 'x':
                print("Tenha um ótimo dia! :)")
                break
            case _:
                print("Entrada inválida!\n")


if __name__ == "__main__":
    main_menu()