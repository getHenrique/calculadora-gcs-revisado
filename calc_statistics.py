# calc_statistisc
# Module D - Statistics operations

from calc_exponenciation import extract_square_root


def average(number_set):


    """Returns the average of a set of values."""

    if not number_set:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        return sum(number_set) / len(number_set)


def median(number_set):


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


def standard_deviation(number_set):

    
    """Returns the standard deviation of a set of values."""

    if not number_set:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        return extract_square_root(
            sum(
                ((value - average(number_set)) ** 2) for value in number_set
            ) / len(number_set)
        )
