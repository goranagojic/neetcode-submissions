class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # constraints
        # positive ints
        # return a minimal lenght of a subarray whose sum is greater or equal to target
        # if no such subarray return 0
        l, r = 0, 0
        s = 0
        min_len = 100001
        while r < len(nums):
            s += nums[r]

            while s >= target:
                min_len = min(min_len, r - l + 1)
                s -= nums[l]
                l += 1
            
            r += 1

        if min_len == 100001:
            min_len = 0

        return min_len

        



        # while r < len(nums) - 1:
        #     print(f"[{l}-{r}], s={s} ")
        #     if s < target:
        #         s += nums[r]
        #         r += 1
        #     elif s > target:
        #         min_len = min(min_len, r - l + 1)
        #         s -= nums[l]
        #         l += 1
        #     else:
        #         min_len = min(min_len, r - l + 1)
        #         r += 1
        #         s += nums[r]
        
        # if min_len == 100001:
        #     min_len = 0
        min_len = min(min_len, r - l + 1)

        return min_len
