class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen={}
        for char in s:
            if char in seen:
                seen[char]+=1
            else:
                seen[char]=1

      
        value_s = sorted(seen.keys(), key=lambda x: seen[x], reverse=True)
        answer=""
        for charac in value_s:
            answer+=charac * seen[charac]
        return answer    


        
