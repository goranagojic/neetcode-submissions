class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = [''] * (len(word1) + len(word2))
        
        i, j, r = 0, 0, 0
        which = 1
        while i < len(word1) and j < len(word2):
            if which == 1:
                result[r] = word1[i]
                i += 1
                which = 2
            else:
                result[r] = word2[j]
                j += 1
                which = 1
            r += 1

        while i < len(word1):
            result[r] = word1[i]
            i, r = i + 1, r + 1
        
        while j < len(word2):
            result[r] = word2[j]
            j, r = j + 1, r + 1

        return "".join(result)

        
