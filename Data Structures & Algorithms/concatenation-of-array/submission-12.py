class Solution:
    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     # time complexity O(n)
    #     # exact time 2*O(n)
    #     ans: List[int] = list()

    #     ans.extend(nums)
    #     ans.extend(nums)

    #     return ans

    def getConcatenation(self, nums: List[int]) -> List[int]:
        # can be done in O(n)
        n = len(nums)
        ans: List[int] = [0] * 2 * n

        for i in range(n):
            ans[i] = nums[i]
            ans[n+i] = nums[i]

        return ans