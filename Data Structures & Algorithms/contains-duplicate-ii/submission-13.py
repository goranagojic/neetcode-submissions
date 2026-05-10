class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) < k + 1:
            return len(set(nums)) != len(nums)

        window = set()
        for l in range(0, len(nums) - k):
            for r in range(0, k + 1):
                num = nums[l+r]
                if num in window:
                    return True
                window.add(num)
            window = set()
            
        return False