class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans: List[int] = list()

        ans.extend(nums)
        ans.extend(nums)

        return ans