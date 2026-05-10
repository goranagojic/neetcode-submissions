from collections import defaultdict

class Solution:
    def hasDuplicate1(self, nums: List[int]) -> bool:
        # time complexity: O(N) because we are iterating over all elements in the array maximaly once
        # space complexity: O(N) - it is actually O(P) P is the number of unique elements in the array

        duplicates = defaultdict(int)
        for num in nums:
            duplicates[num] += 1
            if duplicates[num] > 1:
                return True
        else: 
            return False


    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        