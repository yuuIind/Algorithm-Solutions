def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    
    output = []
    hash_table = {}
    
    for n in nums:
        if n in hash_table:
            hash_table[n] += 1
        else:
            hash_table[n] = 1

    freqs = sorted(hash_table.keys(), key=hash_table.get)

    for i in range(k):
        output.append(freqs[-(i+1)])
        
    return output
