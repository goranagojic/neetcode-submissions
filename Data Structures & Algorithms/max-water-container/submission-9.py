class Solution:
    def maxAreaBruteForce(self, heights: List[int]) -> int:
        # a brute force solution

        p = -1
        for i in range(0, len(heights)-1):
            for j in range(i, len(heights)):
                a = j - i
                b = min(heights[i], heights[j])
                p = max(a * b, p)

        return p


    def maxArea(self, heights: List[int]) -> int:
        p = -1
        i, j = 0, len(heights)-1
        while i < j:
            a = j - i
            b = min(heights[i], heights[j])
            p = max(p, a*b)
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return p


