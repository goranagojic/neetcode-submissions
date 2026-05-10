class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complements = dict() # (complement value, index in array pairs)

        for i in range(len(nums)):
            num = nums[i]

            i_am_complement = num in complements
            if i_am_complement:
                idx = complements[num]
                if i < idx:
                    return [i, idx]
                else:
                    return [idx, i]
            else:
                complements[target - num] = i