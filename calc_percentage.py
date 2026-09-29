# calc_percentage
# Module C - Percentage operations

PERCENT = 100


def percentage_of(reference_value, reference_percentage):


    """Returns the reference percentage of the reference value."""

    return (reference_value * reference_percentage) / PERCENT


def increase(reference_value, increasing_percentage):


    """Returns the increase in the reference value by a increasing percentage."""

    return reference_value + percentage_of(reference_value, increasing_percentage)


def discount(reference_value, discounting_percentage):


    """Returns the discount in the reference value by a discounting percentage."""
    
    return reference_value - percentage_of(reference_value, discounting_percentage)