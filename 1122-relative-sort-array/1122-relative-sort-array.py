class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        output=[]
        count=Counter(arr1)
        for num in arr2:
            output.extend([num]*count[num])
            del count[num]
        for num in sorted(count):
            output.extend([num]*count[num])   
        return output      
             