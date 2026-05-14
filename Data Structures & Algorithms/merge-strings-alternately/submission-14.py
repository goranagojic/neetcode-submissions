class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = [''] * (len(word1) + len(word2))
        i, j = 0, 0

        while i < len(word1) and i < len(word2):
            res[j] = word1[i]
            res[j + 1] = word2[i]
            j += 2
            i += 1

        while i < len(word1):
            res[j] = word1[i]
            j += 1
            i += 1

        while i < len(word2):
            res[j] = word2[i]
            j += 1
            i += 1

        return ''.join(res)
        

