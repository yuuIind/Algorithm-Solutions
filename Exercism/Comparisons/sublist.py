"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2
SUPERLIST = 1
EQUAL = 0
UNEQUAL = -1

def is_subsequence(list_one, list_two):
    for i in range(len(list_two)):
        if list_two[i:i + len(list_one)] == list_one:
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif set(list_two).issubset(set(list_one)):
        if is_subsequence(list_two, list_one):
            return SUPERLIST
        return UNEQUAL
    elif set(list_one).issubset(set(list_two)):
        if is_subsequence(list_one, list_two):
            return SUBLIST
        return UNEQUAL
    else:
        return UNEQUAL
