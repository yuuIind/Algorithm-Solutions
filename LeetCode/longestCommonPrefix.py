def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    s = ""
    key = min(strs, key=len)
    hold = False
    for i, c in enumerate(key):
        for word in strs:
            if word[i] != c:
                hold = True
                break
        if hold: # hold == True -> found non-matching character
            break
        s += c
    return s