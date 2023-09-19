class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_dic = {}
        for i in range(len(nums)):
            if (target-nums[i]) in map_dic:
                return [i, map_dic[target-nums[i]]]
            map_dic[nums[i]] = i
        return []
