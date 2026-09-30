# calc_percentage
# Module C - Percentage operations

PERCENT = 100


def percentage_of(reference_value, reference_percentage):
    """Returns the reference percentage of the reference value."""
    return (reference_value * reference_percentage) / PERCENT


def increase(reference_value, increasing_percentage):
    """Returns the increase in the reference value by a increasing percentage."""
    return (
        reference_value
        + percentage_of(reference_value, increasing_percentage)
    )


def discount(reference_value, discounting_percentage):
    """Returns the discount in the reference value by a discounting percentage."""
    return (
        reference_value
        - percentage_of(reference_value, discounting_percentage)
    )


def percentage_menu():

    user_input = '0'

    while user_input != '4':
        user_input = input(    
            "1 - Percentual\n"
            "2 - Acréscimo\n"
            "3 - Desconto\n"
            "4 - Cancelar operação\n"
            ">> "
        )
        match user_input:
            case '1':
                print("\nPercentual Y de X")
                print(
                    "Y% de X = ",
                    percentage_of(
                        float(input("X = ")),
                        float(input("Y% = "))
                    ),
                    "\n"
                )
            case '2':
                print("\nAcrescentar percentual Y à X")
                print(
                    "X + (X de Y%) = ",
                    increase(
                        float(input("X = ")),
                        float(input("Y% = "))
                    ),
                    "\n"
                )
            case '3':
                print("\nDescontar percentual Y de X")
                print(
                    "X - (X de Y%) = ",
                    discount(
                        float(input("X = ")),
                        float(input("Y% = "))
                    ),
                    "\n"
                )
            case '4':
                print("Saindo do módulo...\n")
                break
            case _:
                print("Input inválido\n")