def square_of_sum(number):
    """Calculate the square of the sum of the first N natural numbers

    :param number: int - any natural number N.
    :return: int - square of the sum of the first N natural numbers.

    """
    sum = (number * (number + 1)
           ) // 2  # sum % 2 always equals to zero, thus it's ok to use '//'
    return sum ** 2


def sum_of_squares(number):
    """Calculate the sum of the squares of the first N natural numbers

    :param number: int - any natural number N.
    :return: int - sum of the squares of the first N natural numbers.

    """

    sum = number * (number + 1) * (2*number + 1)
    return sum // 6


def difference_of_squares(number):
    """Calculate the difference between the square of the sum and the sum of the squares of the first
    N natural numbers

    :param number: int - any natural number N.
    :return: int - difference between the square of the sum and the sum of the squares of the first 
    N natural numbers.

    """
    return square_of_sum(number) - sum_of_squares(number)
