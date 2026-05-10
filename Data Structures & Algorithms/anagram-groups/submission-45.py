class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def getKey(s: str) -> str:

            key = [0] * (ord('z') - ord('a') + 1)
            for c in s:
                key[ord(c) - ord('a')] += 1

            return ''.join(str(key))

        anagrams = dict()

        for s in strs:
            key = getKey(s)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)

        res = [values for _, values in anagrams.items()]
        
        return res
    
