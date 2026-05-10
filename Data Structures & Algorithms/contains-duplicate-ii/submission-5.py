class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        i = 1
        window = set([nums[0]])
        for i in range(1, len(nums)):
            if nums[i] in window:
                return True
            
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
            
        return False