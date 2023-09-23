def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = [1] * len(nums)

    pre = 1
    for i, n in enumerate(nums[:-1]):
        pre *= n
        answer[i+1] = pre
        
    post = 1
    for i, n in enumerate(nums[:0:-1]):
        post *= n 
        answer[-(i+2)] *= post

    return answer
