class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if b.get(complement) != None:
                ret_val = [i, b[complement]] if i < b[complement] else [b[complement], i]
                return ret_val
            b[num] = i     