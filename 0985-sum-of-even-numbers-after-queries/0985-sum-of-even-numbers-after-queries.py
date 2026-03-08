class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        output=[]
        even_num_sum=0
        for i in nums:
            if i%2==0:
                even_num_sum+=i
        for value , index in queries:
            if nums[index]%2 ==0:
               if nums[index] % 2 == 0:
                even_num_sum -= nums[index]
            
            nums[index] += value
            
            if nums[index] % 2 == 0:
                even_num_sum += nums[index]
            
            output.append(even_num_sum)
        
        return output