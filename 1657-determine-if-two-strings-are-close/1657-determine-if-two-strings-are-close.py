class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1_c=Counter(word1)
        word1_c_sorted=sorted(word1_c.values())
        word2_c=Counter(word2)
        word2_c_sorted=sorted(word2_c.values())
        if set(word1)==set(word2) and word1_c_sorted==word2_c_sorted:
            return True
        return False    
