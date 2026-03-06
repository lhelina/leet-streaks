class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_c= Counter(nums)
        for char , count in nums_c.items():
            if count==1:
                return char