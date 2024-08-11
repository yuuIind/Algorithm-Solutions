def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
    total = 0
    prev = 0
    for c in s:
        value = symbols[c]
        if prev < value:
            # prev added at previous iteration, so remove it twice and not once
            total += value - 2 * prev 
        else:
            total += value
        prev = value
    return total