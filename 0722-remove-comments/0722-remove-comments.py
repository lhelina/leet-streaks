class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        result = []
        in_block = False 
        current_line = "" 

        for line in source:
            i = 0
            if not in_block:
                current_line = "" 

            while i < len(line):
                if not in_block  and line[i:i+2] == "/*":
                    in_block = True
                    i += 2

                elif in_block  and line[i:i+2] == "*/":
                    in_block = False
                    i += 2

                elif not in_block and line[i:i+2] == "//":
                    break

                elif not in_block:
                    current_line += line[i]
                    i += 1

                else:
                    i += 1

            if not in_block and current_line:
                result.append(current_line)

        return result