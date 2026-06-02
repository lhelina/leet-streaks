class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        ans = float('inf')

        for i in range(len(landStartTime)):
            lf = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                ans = min(ans, max(waterStartTime[j], lf) + waterDuration[j])

        for j in range(len(waterStartTime)):
            wf = waterStartTime[j] + waterDuration[j]
            for i in range(len(landStartTime)):
                ans = min(ans, max(landStartTime[i], wf) + landDuration[i])

        return ans