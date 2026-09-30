# main menu

from calc_basics import *
from calc_exponenciation import *
from calc_percentage import *
from calc_statistics import *
from calc_conversion import *

def main_menu():


    user_input = '0'

    print("\n=== Calculadora GCS ===\n")
    while user_input != 'x':
        user_input = input(
            "a - Básico\n",
            "b - Potência\n",
            "c - Percentual\n",
            "d - Estatística\n",
            "e - Conversão\n",
            "x - Sair\n",
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
                print("Input inválido\n")

if __name__ == "__main__":
    main_menu()