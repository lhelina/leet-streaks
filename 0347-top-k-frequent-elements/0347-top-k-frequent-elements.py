class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_c=Counter(nums)
        return [num for num, char in nums_c.most_common(k)]

            
        