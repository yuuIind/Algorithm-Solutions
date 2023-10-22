def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    bracket_dict = {'(' : ')', '{' : '}', '[' : ']'}
    bracket_stack = []

    for c in s:
        if c in bracket_dict:
            bracket_stack.append(c)
        elif c in bracket_dict.values():
            if not bracket_stack:
                return False
            top = bracket_stack.pop()
            if bracket_dict[top] != c:
                return False                    
    return not bracket_stack
