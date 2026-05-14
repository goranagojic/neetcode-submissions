class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = [''] * (len(word1) + len(word2))
        p1, p2, p3 = 0, 0, 0

        while p1 < len(word1) and p2 < len(word2):
            res[p3] = word1[p1]
            res[p3 + 1] = word2[p2]
            p3 += 2
            p1, p2 = p1 + 1, p2 + 1

        while p1 < len(word1):
            res[p3] += word1[p1]
            p1, p3 = p1 + 1, p3 + 1

        while p2 < len(word2):
            res[p3] += word2[p2]
            p2, p3 = p2 + 1, p3 + 1

        return ''.join(res)
        

