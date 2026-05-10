class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # input: nums -> positive integers only
        # target: positive intiger
        # return len(sum(minimal subararray)) >= target
        # if no such subarray return 0
        # nonempty nums

        l, r = 0, 0
        s = 0
        min_len = float('inf')
        while r < len(nums):
            
            s += nums[r]
            
            while s >= target:
                min_len = min(min_len, r - l + 1)
                s -= nums[l]
                l += 1

            r += 1

        return 0 if min_len == float('inf') else min_len

            # while s < target:
            #   s += nums[r] # update s
            #   r += 1       # grow window

            # while s > target:
            #   s -= nums[l]
            #   l += 1

            # if s == target:
            #   rembemer the length
