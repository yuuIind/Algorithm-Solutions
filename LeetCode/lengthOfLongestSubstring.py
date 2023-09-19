class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        passed = {}
        start = 0
        length = 0
        for i in range(len(s)):
            c = s[i]
            if c in passed and passed[c] >= start:
                start = passed[c] + 1
            else:
                length = max(length, (i-start+1))
            passed[c] = i
        return length
