class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) < k + 1:
            dupes = set()
            for i in range(len(nums)):
                if nums[i] in dupes:
                    return True
                dupes.add(nums[i])
            return False

        i = 0
        while i < len(nums) - k: # made mistake on this index
            dupes = set()
            
            j = 0
            while j < k + 1:
                if nums[i + j] in dupes:
                    return True
                dupes.add(nums[i + j])
                j += 1
            i += 1

        return False