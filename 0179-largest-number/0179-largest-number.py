class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        nums.sort(reverse=True, key=lambda x: x*10)
        
        result = ''.join(nums)
        
        if result[0] == '0':
            return '0'
        
        return result