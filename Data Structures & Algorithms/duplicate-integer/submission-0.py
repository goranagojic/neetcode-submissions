class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set(nums)
        return len(nums) != len(uniques)
        