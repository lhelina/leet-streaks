class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for ch in ransomNote:
            if ch not in magazine or magazine.count(ch) < ransomNote.count(ch):
                return False
        return True      
