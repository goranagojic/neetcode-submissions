class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # only one valid answer
        complements = dict()
        for i, num in enumerate(nums):
            if num in complements:
                j = complements[num]
                return [i, j] if i < j else [j, i]
            complements[target - num] = i
        
        return
        