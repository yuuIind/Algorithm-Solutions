def equilateral(sides):
    """Determine if a triangle is equilateral
 
    :param sides: list - lengths of the triangle's sides.
    :return: bool - whether a triangle is equilateral or not.
    """
    if sum(sides) < 2 * max(sides) or sum(sides) <= 0:
        return False # not a triangle 
    if len(set(sides)) == 1:
        return True
        
    return False
def isosceles(sides):
    """Determine if a triangle is isosceles
 
    :param sides: list - lengths of the triangle's sides.
    :return: bool - whether a triangle is isosceles or not.
    """
    if sum(sides) < 2 * max(sides) or sum(sides) <= 0:
        return False # not a triangle 
    if len(set(sides)) < 3:
        return True
        
    return False
def scalene(sides):
    """Determine if a triangle is scalene
 
    :param sides: list - lengths of the triangle's sides.
    :return: bool - whether a triangle is scalene or not.
    """
    if sum(sides) < 2 * max(sides) or sum(sides) <= 0:
        return False # not a triangle 
    if len(set(sides)) == 3:
        return True
    return False
