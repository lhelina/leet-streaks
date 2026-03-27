class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        mat_diagonal=defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                mat_diagonal[r+c].append(mat[r][c])
        output=[]
        for k in range(len(mat)+len(mat[0])-1):
            if k%2==0:
                output.extend(mat_diagonal[k][::-1])
            else:
                output.extend(mat_diagonal[k])
        return output      


                    