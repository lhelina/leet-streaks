class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3 != 0:
            return []
        the_middle= num//3
        return [the_middle-1, the_middle , the_middle+1]    