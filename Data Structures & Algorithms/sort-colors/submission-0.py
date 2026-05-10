class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for num in nums:
            buckets[num] += 1

        s = 0
        for val, freq in enumerate(buckets):
            colors = [val] * freq
            e = s + freq + 1
            nums[s:e] = colors
            s += freq
