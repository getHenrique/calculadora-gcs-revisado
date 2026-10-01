# calc_conversion
# Module E - Conversion operations

from value_inputs import get_single_float

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
    """Returns the conversion of a mass from kilograms to pounds.""" 
    return kilograms_mass * KILOGRAMS_TO_POUNDS


def conversion_menu():
    
    user_input: str
    value_input_x: float

    while user_input != '4':
        user_input = input(    
            "1 - Celsisus para Fahrenheit\n"
            "2 - km para milhas\n"
            "3 - kg para libras\n"
            "4 - Cancelar operação\n"
            ">> "
        )
        match user_input:
            case '1':
                print("\nXºC para XºF")
                value_input_x = get_single_float("XºC = ")
                print(
                    "XºF = ",
                    convert_celsius_fahrenheit(value_input_x),
                    "\n"
                )
            case '2':
                print("\nXkm para X milhas")
                value_input_x = get_single_float("XKm = ")
                print(
                    "X milhas = ",
                    convert_kilometers_miles(value_input_x),
                    "\n"
                )
            case '3':
                print("\nXkg para X libras")
                value_input_x = get_single_float("XKg = ")
                print(
                    "X libras = ",
                    convert_kilograms_pounds(value_input_x),
                    "\n"
                )
            case '4':
                print("Saindo do módulo...\n")
                break
            case _:
                print("Entrada inválida!\n")