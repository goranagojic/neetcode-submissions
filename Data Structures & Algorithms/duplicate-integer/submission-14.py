from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicates = defaultdict(int)
        for num in nums:
            duplicates[num] += 1
            if duplicates[num] > 1:
                return True
        else: 
            return False
        