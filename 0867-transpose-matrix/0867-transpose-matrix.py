class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        output=[]
        for c in range(len(matrix[0])):
            row_new=[]
            for r in range(len(matrix)):
                row_new.append(matrix[r][c])
            output.append(row_new)    
        return output        
                