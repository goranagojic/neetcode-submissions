from collections import Counter # gets dictionary from string with characters being keys

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # The idea: iterate over s2 with fixed size window (len(s2)-len(s1)+1) and compare dictionaries of the window and s1
        # Time complexity O(s1_n)*O(s2_n)
        # Spece complexity O(s1_n)

        s1_n, s2_n = len(s1), len(s2)

        if s1_n > s2_n:
            return False
        
        base = Counter(s1)
        for l in range(0, s2_n - s1_n + 1):
            if s2[l] not in base:   # optimization if the character is not in s1, then it cannot be permutation so skip
                continue

            window = Counter(s2[l:l+s1_n])
            if window == base:
                return True

        return False

    def checkInclusion1(self, s1: str, s2: str) -> bool:
        pass
