class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count=Counter(nums)
        for num , count in nums_count.items():
            if count>(len(nums)//2):
                return num


        