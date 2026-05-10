class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # must match the length
        if len(s) != len(t):
            return False

        if set(s) != set(t):
            return False

        hs, ht = dict(), dict()
        for c in s:
            hs[c] = hs.get(c, 0) + 1

        for c in t:
            ht[c] = ht.get(c, 0) + 1

        for c, f in hs.items():
            if f != ht[c]:
                return False
                
        return True

        # compare hashmaps of the characters

