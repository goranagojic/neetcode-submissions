class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return - the length of the longest cocnsecutive sequence

        if nums is None or len(nums) == 0:
            return 0

        unique_values = set(nums) # O(n)

        max_n, n = -float('inf'), 1

        for num in nums:
            predcessor = num - 1
            if predcessor in unique_values:
                continue
            # start of the sequence
            num += 1
            while num in unique_values:
                n += 1
                num += 1
            max_n = max(n, max_n)
            n = 1

        return max(max_n, n)