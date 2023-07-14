def convert(number):
    """ Convert a number into a string that contains raindrop sounds corresponding to certain potential
    factors.

    :param number: int - a number that evenly divides into another number.
    :return: str - a string that contains raindrop sounds corresponding factor.
    """
    factor_sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    
    sound_list = [factor for factor in factor_sounds.keys() if number % factor == 0]
    if not sound_list:
        return str(number)
    else:
        return "".join([factor_sounds[factor] for factor in sound_list])
