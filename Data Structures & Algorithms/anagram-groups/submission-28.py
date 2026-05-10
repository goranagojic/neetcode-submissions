from collections import defaultdict

class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        # time complexity: N * KlogK (K-string length, N is number of strings in the input array)

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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list) # key: an letter array, value: a list of anagrams with key combination

        for s in strs:
            key = [0] * 26 # 26 lowercase characters
            for c in s:
                idx = ord(c) - ord('a')
                key[idx] += 1

            anagrams[tuple(key)].append(s)

        return list(anagrams.values())