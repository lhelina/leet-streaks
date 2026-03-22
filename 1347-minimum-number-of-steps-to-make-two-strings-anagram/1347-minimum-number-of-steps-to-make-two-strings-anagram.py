class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        output=0
        s_count=Counter(s)
        t_count=Counter(t)
        for value in t_count:
            if t_count[value]>s_count[value]:
                output+=t_count[value]-s_count[value]
        return output        
            
