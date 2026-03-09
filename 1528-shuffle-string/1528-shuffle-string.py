class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n=len(s)
        output=['']*n
        for i in range(n):
            output[indices[i]]=s[i]
        return ''.join(output)

            