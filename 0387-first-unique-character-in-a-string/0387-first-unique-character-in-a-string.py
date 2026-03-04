from collections import Counter;
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_s=Counter(s)
        for i , ch in enumerate(s):
            if char_s[ch]==1:
                return i
        return -1        

