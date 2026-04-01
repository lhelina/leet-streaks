class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def rotate(matrix):
           
            for i in range(len(matrix)):
                for j in range(i,len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for row in matrix:
                row.reverse()
        
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False       
