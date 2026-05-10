from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        base = Counter(s1)

        r = 0
        while r < (len(s2) - len(s1) + 1):
            if s2[r] not in base:
                r += 1
                continue

            window = dict()
            l = 0
            # populate window
            while l < len(s1):
                window[s2[r+l]] = window.get(s2[r+l], 0) + 1
                l += 1
            # check if window equals to base
            if base == window:
                return True
            r += 1 

        return False
        