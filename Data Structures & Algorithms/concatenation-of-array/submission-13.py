class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # in:  nums, len n
        # out: ans len 2n

        ans = []
        for i in range(0, 2):
            for num in nums:
                ans.append(num)

        return ans