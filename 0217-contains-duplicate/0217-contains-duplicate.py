class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts=[]
        nums_count=Counter(nums)
        for num, count in nums_count.items():
            if count > 1:
                counts.append(counts)
           
        if (counts):
            return True 
        else:
            return False      