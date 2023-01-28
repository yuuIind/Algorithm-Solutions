def leap_year(year):
    """ Given a year, report if it is a leap year.
 
    :parameter year: int - the year
    :return: bool - whether a year is a leap year or not
    """
    return year %  4 == 0 and (year % 100 != 0 or year % 400 == 0)
