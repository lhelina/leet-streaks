class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen=[]
        for i in nums1:
            if i in nums2:
                seen.append(i)
        set_seen=set(seen)        
        return list(set_seen)       
        