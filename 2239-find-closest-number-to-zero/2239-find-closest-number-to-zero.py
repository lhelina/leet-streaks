class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        absolutes = []
        for num in nums:
            absolute = abs(num)
            absolutes.append(absolute)

        minimum = min(absolutes)

        indexes = [i for i, v in enumerate(absolutes) if v == minimum]

        return max(nums[i] for i in indexes)  
        