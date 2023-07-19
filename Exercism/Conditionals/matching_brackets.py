def is_paired(input_string):
    brackets = []
    for c in input_string:
        if c == "[" or c == "(" or c == "{":
            brackets.append(c)
            continue
        if c == "]" or c == ")" or c == "}":
            bracket = brackets.pop(-1) if len(brackets) > 0 else ""
            if c == "]" and bracket == "[":
                continue
            elif c == ")" and bracket == "(":
                continue
            elif c == "}" and bracket == "{":
                continue
            else:
                return False
    
    return len(brackets) == 0
