class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        subarray_sum=sum(nums[:k])
        maximum=subarray_sum
        for i in range(k,len(nums)):
            subarray_sum+=(nums[i])
            subarray_sum-=nums[i-k]
            if subarray_sum > maximum:
                maximum=subarray_sum
        return maximum/float(k) 
