from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 1) sort strings
        sorted_strs = ["".join(sorted(s)) for s in strs]

        # 2) populate hashmap
        anagrams = defaultdict(list)
        for key, value in zip(sorted_strs, strs):
            anagrams[key].append(value)

        # 3) form the list
        ret_val = list()
        for k, value in anagrams.items():
            ret_val.append(value)

        # return the list
        
        return ret_val