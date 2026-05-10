class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        # in: strs - array of strings
        # out: list of anagrams
        # time complexity: O(n * mlogm)

        anagrams = dict()

        for s in strs: # n
            key = ''.join(sorted(s)) # mlogm
            if key not in anagrams:
                anagrams[key] = [] # 1
            anagrams[key].append(s) # 1

        res = [values for _, values in anagrams.items()] # n

        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Groups anagrams in a string."""
        # avg. time complexity: O(n) * O(m) = O(nm), n number of string, m string lenght

        def getKey(s: str) -> str:
            """Returns a string representation of 28 element list with character counts for each letter."""
            # time complexity: O(m) where m is string length
            key = [0] * (ord('z') - ord('a') + 1)
            for c in s:
                key[ord(c) - ord('a')] += 1

            return str(key)

        anagrams = dict()

        for s in strs: # n
            key = getKey(s) # n * m 
            if key not in anagrams:
                anagrams[key] = []  # n * m * 1
            anagrams[key].append(s) # n * m * 1

        res = [values for _, values in anagrams.items()] # n
        
        return res
    
