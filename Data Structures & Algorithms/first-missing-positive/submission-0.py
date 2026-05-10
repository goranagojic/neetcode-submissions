class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for num in range(1, 2**31-1):
            if num not in nums:
                return num

        return 2**31
