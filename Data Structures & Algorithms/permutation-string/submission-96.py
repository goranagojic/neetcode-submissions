class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
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