def square(number):
    """
    :param number: int - number of the given square.
    :return: int - amount of grains on the given square.

    Calculates the number of grains of wheat on a given square.
    if 'number' is not between 1 and 64, raises a ValueError exception
    """
    if (number < 1) or (number > 64):
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    """

    :return: int - amount of grains on the given square.

    Calculates the total number of grains on the chessboard
    """
    total_amount = 0
    for i in range(1, 65):
        total_amount += square(i)
    return total_amount
