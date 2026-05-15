class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # input: nums sorted in non-decreasing order
        # remove duplicates in-place
        # return number of unique elements
        # array elem. can be both positive and negative
        # The idea: do inplace logical removal by two pointers. The first points to the current element, the second on the next different element.
        # whenever these two pointers differ, copy from the second to the first.
        # In steps: move the second pointer while both numbers are the same. When they are different, copy from the second to the first, and move pointers.
        
        i, j = 0, 0
        while j < len(nums):

            while j < len(nums) and nums[i] == nums[j]: # skip while numbers are the same
                j += 1
                
            if j == len(nums):  # if out of bounds, exit by proceeding to the while loop that checks j bounds
                break

            i += 1
            nums[i] = nums[j]   # copy

        return i + 1