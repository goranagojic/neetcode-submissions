from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 1) sort strings
        # time complexity O(N*KlogK)  - N strings of length K (sorting is KlogK, for N strings makes O(NKlogK))
        sorted_strs = ["".join(sorted(s)) for s in strs]

        # 2) populate hashmap
        # probable time complexity O(N)
        anagrams = defaultdict(list)
        for key, value in zip(sorted_strs, strs):
            anagrams[key].append(value)

        # return the list
        return list(anagrams.values()) # so, the total time complexity of the solution is time complexity of the sorting algorithm