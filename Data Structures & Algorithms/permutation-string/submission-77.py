import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # NONOPTIMAL SOLUTION
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

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # OPIMAL SOLUTION
        # time complexity: O(n) where n is length of s2
        # space complexity: O(1) because it uses two dictionaries of constant size (26)

        if len(s1) > len(s2):
            return False

        m = len(s1)

        # create and populate count dictionaries for s1 and s2
        s1_count = {c: freq for c, freq in zip(list(string.ascii_lowercase), [0] * 26)}
        for c in s1:
            s1_count[c] += 1

        s2_count = {c: freq for c, freq in zip(list(string.ascii_lowercase), [0] * 26)}
        s2_count = {chr(c): 0 for c in range(ord('a'),ord('z')+1)}

        l, r = 0, 0
        matches = 0
        while r < len(s2) - len(s1) + 1:
            if matches == 26: return True
            if r == 0:
                l = 0
                # Here is one O(m) loop, but it happens once so it can be ommited from the total time complexity
                while l < len(s1):
                    s2_count[s2[r+l]] = s2_count.get(s2[r+l], 0) + 1
                    l += 1

                # count matches
                for c in s2_count.keys():
                    if s1_count[c] == s2_count[c]:
                        matches += 1
            else:
                # remove previous beginning of the window that is now out of scope
                print(f"r-1 {s2[r-1]}, r = {s2[r]}")
                c = s2[r-1]
                s2_count[c] -= 1
                # correct matches
                if s1_count[c] == s2_count[c]:
                    matches += 1
                elif s1_count[c] - 1 == s2_count[c]:
                    matches -= 1
                # add new char to window
                c = s2[r + m - 1]
                s2_count[c] += 1
                # correct matches
                if s1_count[c] == s2_count[c]:
                    matches += 1
                elif s1_count[c] + 1 == s2_count[c]:
                    matches -= 1
            r += 1
        
        return matches == 26