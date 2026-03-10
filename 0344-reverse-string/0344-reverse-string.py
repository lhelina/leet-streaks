class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        reversed_s=[s[index]for index in range (len(s)-1,-1,-1)]
        for i in range(len(s)):
            s[i]=reversed_s[i]