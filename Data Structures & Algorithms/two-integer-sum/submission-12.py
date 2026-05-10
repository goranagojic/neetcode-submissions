class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if complements.get(complement) != None:
                c_idx = complements[complement]
                ret_val = [i, c_idx] if i < c_idx else [c_idx, i]
                return ret_val
            complements[num] = i     