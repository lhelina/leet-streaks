class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles) // 3
        res = 0
        
        index = len(piles) - 2  
        
        for _ in range(n):
            res += piles[index]
            index -= 2 
        
        return res