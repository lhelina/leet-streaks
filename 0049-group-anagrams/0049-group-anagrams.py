class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups_a = defaultdict(list)
        for string in strs:
            the_key="".join(sorted(string))
            groups_a[the_key].append(string)
        return list(groups_a.values())  

                