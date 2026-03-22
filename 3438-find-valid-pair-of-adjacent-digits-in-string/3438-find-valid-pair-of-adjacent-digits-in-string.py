class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_count = Counter(s)   
        pairs = []
        for i in range(len(s) - 1):
            pairs.append(s[i] + s[i+1])

        for pair in pairs:
            if pair[0] != pair[1]:  
                if (s_count[pair[0]] == int(pair[0]) and 
                    s_count[pair[1]] == int(pair[1])):   
                        return pair
                        break
            
        return ""    