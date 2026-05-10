import bisect

class Solution:
    def minSubArrayLenSliding(self, target: int, nums: List[int]) -> int:
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


    def minSubArrayLenDict(self, target: int, nums: List[int]) -> int:

        prefix_lookup = dict()

        s = 0
        min_len = float('inf')
        for r in range(0, len(nums)):
            # print(f"s={s}, prefix_lookup: {prefix_lookup}")
            s += nums[r]
            prefix_lookup[s] = r
            
            if s >= target:
                min_len = min(min_len, r + 1)
                target_prefix = s - target
                for prefix, psum in prefix_lookup.items():
                    if prefix > target_prefix:
                        continue
                    min_len = min(min_len, r - psum)

        return min_len if min_len != float('inf') else 0


    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # create prefix sums
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        min_len = float('inf')
        for r in range(1, len(prefix)):

            needed = prefix[r] - target
            l = bisect.bisect_right(prefix, needed, 0, r) - 1
            if l >= 0:
                min_len = min(min_len, r - l)

        return min_len if min_len != float('inf') else 0

        
