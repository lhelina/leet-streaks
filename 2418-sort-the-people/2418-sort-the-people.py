class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        n=len(heights)
        for i in range(len(heights)):
            min_index=i
            for j in range(i+1, n ):
                if heights[min_index]<heights[j]:
                    min_index=j
            heights[i],heights[min_index]=heights[min_index],heights[i]
            names[i],names[min_index]=names[min_index],names[i]
        return names           

        
                
        