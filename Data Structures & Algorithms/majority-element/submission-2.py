from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        threashold = len(nums) / 2
        for num, cnt in counts.items():
            if cnt > threashold:
                return num
            
        return nums[0]
        