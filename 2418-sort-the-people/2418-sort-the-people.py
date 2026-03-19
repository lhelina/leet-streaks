class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        n=len(heights)
        for passnum in range(len(heights)):
            for i in range(n-1-passnum):
                if heights[i]<heights[i+1]:
                    heights[i],heights[i+1]=heights[i+1],heights[i]
                    names[i],names[i+1]=names[i+1],names[i]
        return names            

        
                
        