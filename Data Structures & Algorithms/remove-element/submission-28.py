class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not len(nums):
            return 0

        if len(nums) == 1 and nums[0] == val:
            return 0

        j = len(nums)-1 # start substituting from the end
        for i in range(len(nums)):
            if nums[i] == val:
            
                while j > 0 and nums[j] == val:
                    j -= 1

                if j <= i:
                    return i 

                nums[i], nums[j] = nums[j], nums[i]

        return j + 1