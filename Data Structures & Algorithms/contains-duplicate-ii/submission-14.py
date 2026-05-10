class Solution:
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:

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

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) < k + 1:
            return len(set(nums)) != len(nums)

        window = set()
        
        for i in range(0, k + 1):
            num = nums[i]
            if num in window:
                return True
            window.add(num)

        l, r = 0, k + 1
        while r < len(nums):
            window.remove(nums[l])
            l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
            r += 1

        return False