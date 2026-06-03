class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def calc(start1, dur1, start2, dur2):
            min_end = min(start1[i] + dur1[i] for i in range(len(start1)))
            ans = float('inf')

            for i in range(len(start2)):
                ans = min(ans, max(min_end, start2[i]) + dur2[i])

            return ans

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )