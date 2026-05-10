class Solution:

    def removeElementTwoPointersComplex(self, nums: List[int], val: int) -> int:
        # time complexity O(N)
        # This is more complex solution that replaces val values looking from the left with non-val values looking from the righ
        # Two-pointer pattern. Overkill for this task

        if not len(nums):
            return 0

        if len(nums) == 1 and nums[0] == val:
            return 0

        j = len(nums)-1 # start substituting from the end
        for i in range(len(nums)): 
            if nums[i] == val:
            
                while j >= i and nums[j] == val:
                    j -= 1

                if j <= i:
                    return i 

                nums[i], nums[j] = nums[j], nums[i]

        return j + 1

    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1

        return n


    def removeElementTwoPointersI(self, nums: List[int], val: int) -> int:
        # time complexity O(n)
        # this is the easiest solution that moves all non-val values to the left
        current_idx = 0
        for num in nums:
            if num != val:
                nums[current_idx] = num
                current_idx += 1
            
        return current_idx