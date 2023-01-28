def is_armstrong_number(number):
    """Checks whether a given number is an Armstron number or not.

    :param number: int - any positive number.
    :return: bool - whether 'number' is an Armstrong number or not.

    Function that takes an integer number and checks if the sum of its own digits each raised to the
    power of the number of digits is equal to the 'number' itself. Then, returns a boolean according to
    check.
    """
    number_in_string = str(number)
    number_of_digits = len(number_in_string)
    digits = [int(digit) ** number_of_digits for digit in number_in_string]
    return number == sum(digits)
