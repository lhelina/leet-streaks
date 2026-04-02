class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i=0
        j=int(c**0.5)
        while i<=j:
            if i*i + j*j==c:
                return True 
            if i*i + j*j < c:
                i+=1
            else:
                j-=1
        return False                 
