class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        seen={}

        for response in responses:
            response_n=set(response)
            for word in response_n:
                if word in seen:
                    seen[word] += 1
                else:
                    seen[word] = 1
        max_count = max(seen.values())  
        answer=""
        for word in seen:
            if seen[word]==max_count:
                if answer=="" or word<answer:
                    answer=word
        return answer         



                