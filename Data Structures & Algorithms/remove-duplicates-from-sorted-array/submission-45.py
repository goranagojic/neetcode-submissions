class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # input: nums sorted in non-decreasing order
        # remove duplicates in-place
        # return number of unique elements
        # array elem. can be both positive and negative

        # TODO handle zero array case
        
        i, j = 0, 0
        while j < len(nums):

            while j < len(nums) and nums[i] == nums[j]: # skip while they are same
                j += 1
                
            if j == len(nums):
                continue

            i += 1
            nums[i] = nums[j]

        return i + 1