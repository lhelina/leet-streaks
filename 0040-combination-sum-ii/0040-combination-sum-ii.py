class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Choose
                path.append(candidates[i])
                
                # Explore (move to next index)
                backtrack(i + 1, path, remaining - candidates[i])
                
                # Un-choose
                path.pop()
        
        backtrack(0, [], target)
        return res