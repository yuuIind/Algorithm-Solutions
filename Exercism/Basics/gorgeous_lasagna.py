EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return int(EXPECTED_BAKE_TIME - elapsed_bake_time)


def preparation_time_in_minutes(number_of_layers):
    """Calculate the bake time remaining.
 
    :param number_of_layers: int - number of layers to add to the lasagna.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.
 
    Function that takes the number of layers you want to add to the lasagna as an argument and 
    returns how many minutes you would spend making them based on the 'PREPARATION_TIME'.
    """
    return int(number_of_layers * PREPARATION_TIME)
    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :param number_of_layers: int - number of layers to add to the lasagna.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.
 
    Function that takes the number of layers you want to add to the lasagna and the actual minutes 
    the lasagna has been in the oven as an arguments and returns the total number of minutes you've
    been cooking.
    """
    
    sum = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return int(sum)
    
