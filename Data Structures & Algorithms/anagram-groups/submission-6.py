class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = [(''.join(sorted(s)), s) for s in strs]
        anagrams = dict()
        for ss, s in sorted_strings:
            if anagrams.get(ss) is None:
                anagrams[ss] = list()
            anagrams[ss].append(s)

        ret_val = list()
        for k, s in anagrams.items():
            ret_val.append(s)

        return ret_val


