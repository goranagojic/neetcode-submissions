class Solution:
    def getConcatenation1(self, nums: List[int]) -> List[int]:
        # in:  nums, len n
        # out: ans len 2n

        ans = []
        for i in range(0, 2):
            for num in nums:
                ans.append(num)

        return ans

    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(0, n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
