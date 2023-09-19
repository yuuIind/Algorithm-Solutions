class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        total_len = (len1 + len2)
        if total_len < 2:
            return nums1[0] if nums1 else nums2[0]
        median_index = total_len // 2
        merged_list = []
        i = 0
        j = 0
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                merged_list.append(nums1[i])
                i += 1
            else:
                merged_list.append(nums2[j])
                j += 1

        while i < len1:
            merged_list.append(nums1[i])
            i += 1
        
        while j < len2:
            merged_list.append(nums2[j])
            j += 1
        
        if (len1 + len2) % 2 == 0:
            return (merged_list[median_index] + merged_list[median_index-1]) / 2.0
        return merged_list[median_index] 
         
