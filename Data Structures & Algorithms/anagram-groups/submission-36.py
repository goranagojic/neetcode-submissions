class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # in: strs - array of strings
        # out: list of anagrams

        anagrams = dict()

        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)

        res = [values for _, values in anagrams.items()]

        return res