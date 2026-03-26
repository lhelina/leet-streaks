class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        index_rows = set()
        index_cols = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    index_rows.add(r)
                    index_cols.add(c)
        for r in index_rows:
            matrix[r]=[0]*len(matrix[0])    
        for c in index_cols:
            for r in range(len(matrix)):
                matrix[r][c]=0
        
