class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in nums:
            for j in str(i):
                output.append(int(j))
        return output     

           
