# calc_percentage
# Module C - Percentage operations

PERCENT = 100


def percentage_of(reference_value, reference_percentage):


    return (reference_value * reference_percentage) / PERCENT


def increase(reference_value, increase_percentage):


    return reference_value + percentage_of(reference_value, increase_percentage)


def discount(reference_value, discount_percentage):

    
    return reference_value - percentage_of(reference_value, discount_percentage)