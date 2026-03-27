class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        diagonals = defaultdict(list)
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                diagonals[r + c].append(mat[r][c])
        
        result = []
        
        for k in range(len(mat) + len(mat[0]) - 1):
            if k % 2 == 0:
                result.extend(diagonals[k][::-1])  
            else:
                result.extend(diagonals[k])
        
        return result