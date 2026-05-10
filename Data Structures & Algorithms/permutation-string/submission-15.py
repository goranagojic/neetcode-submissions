from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed size window of size len(s1)

        s1_n, s2_n = len(s1), len(s2)

        if s1_n > s2_n:
            return False
        
        base = Counter(s1)
        for l in range(0, s2_n - s1_n + 1):
            print(l)
            if s2[l] not in base:   # if the character is not in s1, then it cannot be permutation so skip
                continue

            window = Counter(s2[l:l + s1_n])
            print(f"base: {base}, window: {window}")
            if window == base:
                return True

        return False