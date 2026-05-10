import string

from collections import Counter

class Solution:
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        # space complexity: O(m) where m is the length of the s1 string
        # time complexity: O(mn) where n is the length of the s2 string
        # since strings may contain only lowercase engl. letters, then time complexity is O(n) because O(m) can be approximated as O(1)
        base = Counter(s1)

        r = 0
        while r < (len(s2) - len(s1) + 1):
            # if the first character is not in the base, the window won't be as well
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

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        m = len(s1)

        # create and populate count dictionaries for s1 and s2
        s1_count = {c: freq for c, freq in zip(list(string.ascii_lowercase), [0] * 26)}
        for c in s1:
            s1_count[c] += 1

        s2_count = {c: freq for c, freq in zip(list(string.ascii_lowercase), [0] * 26)}

        l, r = 0, 0
        matches = 0
        while r < len(s2) - len(s1) + 1:
            if matches == 26: return True
            if r == 0:
                l = 0
                while l < len(s1):
                    s2_count[s2[r+l]] = s2_count.get(s2[r+l], 0) + 1
                    l += 1

                # count matches
                for c in s2_count.keys():
                    if s1_count[c] == s2_count[c]:
                        matches += 1
            else:
                # remove old left
                print(f"r-1 {s2[r-1]}, r = {s2[r]}")
                c = s2[r-1]
                s2_count[c] -= 1
                # correct matches
                if s1_count[c] == s2_count[c]:
                    matches += 1
                elif s1_count[c] - 1 == s2_count[c]:
                    matches -= 1
                # add new right
                c = s2[r + m - 1]
                s2_count[c] += 1
                # correct matches
                if s1_count[c] == s2_count[c]:
                    matches += 1
                elif s1_count[c] + 1 == s2_count[c]:
                    matches -= 1
            r += 1
        
        return matches == 26
        