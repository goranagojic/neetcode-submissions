class Solution:
    def _indices(self, i, j):
        if i > j:
            return [j, i]
        return [i, j]


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return self._indices(i, j)
                j = j + 1
            i = i + 1