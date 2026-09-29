# calc_statistisc
# Module D - Statistics operations

from calc_exponenciation import extract_square_root


def average(set):


    """ Returns the average of a set of values
    """

    if not set:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        return sum(set) / len(set)


def median(set):


    """ Returns the median of a set of values.
    """

    if not set:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        sorted_set = sorted(set)
        set_size = len(sorted_set)
        if (set_size % 2) == 0:
            return (
                sorted_set[(set_size // 2) - 1]
                + sorted_set[set_size // 2]
            ) / 2
        else:
            return sorted_set[set_size // 2]


def standard_deviation(set):

    
    """ Returns the standard deviation of a set of values.
    """

    if not set:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        return extract_square_root(
            sum(
                ((value - average(set)) ** 2) for value in set
            ) / len(set)
        )
