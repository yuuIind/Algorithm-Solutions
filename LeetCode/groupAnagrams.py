def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    hash_table = {}

    for s in strs:
        key = "".join(sorted(s)) 
        if key in hash_table:
            hash_table[key].append(s)
        else:
            hash_table[key] = [s,]

    return hash_table.values()
