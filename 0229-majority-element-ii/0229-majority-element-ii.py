class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        nums_count=Counter(nums)
        for num, count in nums_count.items():
            if count > len(nums)//3:
                output.append(num)
        return output
                
        