from collections import Counter

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        players=[]
        losers=[]
        answer=[] 
        for winner, loser in matches:
            players.append(winner)
            players.append(loser)
            losers.append(loser)
        result = sorted(list(set(players) - set(losers)))
        answer.append(result)
        count_loser=Counter(losers)
        counts_lost_once=sorted([player for player,count in count_loser.items() if count==1])
        answer.append(counts_lost_once)
        return answer
        

         
                

                
