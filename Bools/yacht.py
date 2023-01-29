CHOICE = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
YACHT = 11
def score(dice, category):
    """ Calculates the score of the dice game Yacht according to given category
 
    :param dice: list - values for five dice roll.
    :param category: int - scoring category.
    :return: int - score of the dice for that category.
 
    """
    if category in range(ONES, SIXES + 1):
        return category * dice.count(category)
    elif category == CHOICE:
        return sum(dice)
    elif category in range(FULL_HOUSE, YACHT + 1):
        dice_set = set(dice)
        if len(dice_set) == 1 and category in (YACHT, FOUR_OF_A_KIND):
            return 50 if category == YACHT else 4 * max(dice_set, key=dice.count)
        elif len(dice_set) == 2 and category in (FULL_HOUSE, FOUR_OF_A_KIND):
            if category == FULL_HOUSE and dice.count(list(dice_set)[0]) in [2, 3]:
                return sum(dice)
            elif category == FOUR_OF_A_KIND and dice.count(list(dice_set)[0]) in [1, 4]:
                return 4 * max(dice_set, key=dice.count)
        elif len(dice_set) == 5 and not set([1, 6]).issubset(dice_set):
            if category == BIG_STRAIGHT and 6 in dice_set:
                return 30
            elif category == LITTLE_STRAIGHT and 1 in dice_set:
                return 30
        return 0
