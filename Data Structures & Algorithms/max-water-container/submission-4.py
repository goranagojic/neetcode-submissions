class Solution:
    def maxArea(self, heights: List[int]) -> int:

        p= -1

        for i in range(0, len(heights)-1):
            for j in range(i, len(heights)):
                a = j - i
                b = min(heights[i], heights[j])
                p = max(a * b, p)

        return p


        