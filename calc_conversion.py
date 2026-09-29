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