class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        teams=[]
        skill_so=sorted(skill)
        target=skill_so[0]+skill_so[-1]
        for i in range(len(skill_so)//2):
            j=len(skill_so)-1-i
            if skill_so[i]+skill_so[j]!=target:
                return -1
            teams.append([skill_so[i],skill_so[j]])    
        output=0     
        for team in teams:
            output+=team[0]*team[1] 
        return output                            
                    

        