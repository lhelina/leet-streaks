class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        no_duplicate = set()
        twice_num = []
        
        for num in nums:
            if num in no_duplicate:
                twice_num.append(num)
            else:
                no_duplicate.add(num)
                
        return twice_num