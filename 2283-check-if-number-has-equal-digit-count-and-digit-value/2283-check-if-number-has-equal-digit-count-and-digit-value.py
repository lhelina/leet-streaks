
class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for index, digit in enumerate(num):
            if num.count(str(index)) != int(digit):
                return False
        return True