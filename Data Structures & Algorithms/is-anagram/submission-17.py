class Solution:
    def isAnagramHahsmaps(self, s: str, t: str) -> bool:
        # must match the lengtt
        if len(s) != len(t):
            return False

        hs, ht = dict(), dict()
        for c in s:
            hs[c] = hs.get(c, 0) + 1

        for c in t:
            ht[c] = ht.get(c, 0) + 1

        if ht.keys() != hs.keys(): # there are different characters in s and t
            return False

        for c, f in hs.items():
            if f != ht[c]:
                return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sa, ta = [0] * (ord('z') - ord('a') + 1), [0] * (ord('z') - ord('a') + 1)
        
        for cs, ct in zip(s, t):
            sa[ord(cs) - ord('a')] += 1
            ta[ord(ct) - ord('a')] += 1

        return sa == ta

