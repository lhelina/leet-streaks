class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        rows=[]
        for row in image:
           rows.append(row[::-1])
        
        for r in range(len(rows)):
            for c in range(len(rows[0])):
                if rows[r][c] == 0:
                    rows[r][c] = 1
                else:
                    rows[r][c] = 0
        
        return rows