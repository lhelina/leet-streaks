class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0:
            return 0
        points.sort(key=lambda x:x[1])
        count=1
        arrow_pointed=points[0][1]   
        for i in range(1,len(points)):
            if points[i][0]>arrow_pointed:
                count+=1
                arrow_pointed=points[i][1]
        return count         
