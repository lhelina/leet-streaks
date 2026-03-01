class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = 0
        
        for word in words:
            temp_chars = list(chars) 
            word_forming = ""       
            
            for ch in word:
                if ch in temp_chars:
                    word_forming += ch
                    temp_chars.remove(ch)  
                else:
                    break  
            
            if word_forming == word:  
                count += len(word)
        
        return count