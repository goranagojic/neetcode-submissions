class Solution:
    def checkInclusionBruteForce(self, s1: str, s2: str) -> bool:
        # 18 minutes, with help - had logical error. used set instead of dict
        
        if len(s1) > len(s2):
            return False

        # reference = {ch: s1.count(ch) for ch in s1}
        reference = dict()
        for ch in s1:
            reference[ch] = reference.get(ch, 0) + 1

        for i in range(0, len(s2) - len(s1) + 1):
            window = dict()
            for j in range(0, len(s1)):
                window[s2[i+j]] = window.get(s2[i+j], 0) + 1

            print(f"window: {window}")
            print(f"reference: {reference}")
            
            if window == reference:
                return True

        return False

    def checkInclusionFailure(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        reference = dict()
        for ch in s1:
            reference[ch] = reference.get(ch, 0) + 1

        l, r = 0, len(s1) # r is exclusive
        window = dict()
        for i in range(l, r):
            window[s2[i]] = window.get(s2[i], 0) + 1
        print(window)

        while r < len(s2):
            if window == reference:
                return True
            window.pop(s2[l])
            l += 1
            window[s2[r]] = window.get(s2[r], 0) + 1
            r += 1
            print(window)

        return False


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # dictionary for s1
        reference = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        for ch in s1:
            reference[ch] = reference.get(ch, 0) + 1

        # dictionary for window
        window = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        for i in range(0, len(s1)):
            ch = s2[i]
            window[ch] = window.get(ch, 0) + 1

        # print(reference)
        # print(window)

        matches = sum([1 for ch in window.keys() if window[ch] == reference[ch]])

        # loop through the rest of s2, removing left and adding right elem until matches are different than 26 (eng. alph. len)
        l, r  = 0, len(s1)
        while r < len(s2):
            if matches == 26:
                return True

            cl = s2[l]
            window[cl] -= 1
            if window[cl] == reference[cl]:
                matches += 1
            elif window[cl] + 1 == reference[cl]:
                matches -= 1
            l += 1

            cr = s2[r]
            window[cr] += 1
            if window[cr] == reference[cr]:
                matches += 1
            elif window[cr] - 1 == reference[cr]:
                matches -= 1
            r += 1

            print(window)

        # matches are checked to see if permutation is found, not dicts

        return matches == 26