def steps(number):
    """

    :param number: int - starting value.
    :return: int - number of steps required to reach 1.

    Function that takes any positive integer n as an argument and returns the number of steps required
    to reach 1 according to the Collatz Conjecture.
    """
    if (number <= 0):
        raise ValueError("Only positive integers are allowed")
    number_of_steps = 0

    while number != 1:
        if (number % 2) == 0:
            number = number // 2
            number_of_steps += 1
        else:
            number = (3 * number) + 1
            number_of_steps += 1

    return number_of_steps
