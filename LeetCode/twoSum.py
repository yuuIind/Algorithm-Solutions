class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_dic = {}
        for i, n in enumerate(nums):
            if (target-n) in map_dic:
                return [i, map_dic[target-n]]
            map_dic[n] = i
        return []
