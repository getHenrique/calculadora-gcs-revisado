# calc_conversion
# Module E - Conversion operations

CELSIUS_FAHRENHEIT_SCALING_FACTOR = 9 / 5
CELSIUS_FAHRENHEIT_OFFSET = 32
KILOMETERS_TO_MILES = 0.621371
KILOGRAMS_TO_POUNDS = 2.20462


def convert_celsius_fahrenheit(celsius_temperature):
    """Returns the conversion of a temperature from celsius to fahrenheit."""


    return (
        celsius_temperature * CELSIUS_FAHRENHEIT_SCALING_FACTOR
        + CELSIUS_FAHRENHEIT_OFFSET
    )


def convert_kilometers_miles(kilometers_distance):
    """Returns the conversion of a distance from kilometers to miles."""


    return kilometers_distance / KILOMETERS_TO_MILES


def convert_kilograms_pounds(kilograms_mass):
    """Returns the conversion of a mass from kilograms to punds."""

    
    return kilograms_mass * KILOGRAMS_TO_POUNDS


def conversion_menu():
    
    
    user_input = '0'

    while user_input != '4':
        user_input = input(    
            "1 - Celsisus para Fahrenheit\n",
            "2 - km para milhas\n",
            "3 - kg para libras\n",
            "4 - Cancelar operação\n",
            ">> "
        )
        match user_input:
            case '1':
                print("\nXºC para XºF")
                print(
                    "XºF = ",
                    convert_celsius_fahrenheit(
                        float(input("XºC = ")),
                    ),
                    "\n"
                )
            case '2':
                print("\nXkm para X milhas")
                print(
                    "X milhas = ",
                    convert_kilometers_miles(
                        float(input("Xkm = ")),
                    ),
                    "\n"
                )
            case '3':
                print("\nXkg para X libras")
                print(
                    "X libras = ",
                    convert_kilograms_pounds(
                        float(input("Xkg = ")),
                    ),
                    "\n"
                )
            case '4':
                print("Saindo do módulo...\n")
                break
            case _:
                print("Input inválido\n")