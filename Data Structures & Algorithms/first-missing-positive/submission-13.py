class Solution:
    def merge(self, nums, s, m, e):
        left, right = nums[s:m], nums[m:e]
        li, ri, i = 0, 0, s

        while li < len(left) and ri < len(right):
            if left[li] <= right[ri]:
                nums[i] = left[li]
                li = li + 1
            else:
                nums[i] = right[ri]
                ri = ri + 1
            i = i + 1

        while li < len(left):
            nums[i] = left[li]
            li = li + 1
            i = i + 1

        while ri < len(right):
            nums[i] = right[ri]
            ri = ri + 1
            i = i + 1

        return nums


    def mergesort(self, nums, s, e):
        # stop when 0 or 1 elements in list, s - inclusive, e - exclusive
        if e - s <= 1:
            return nums

        m = (s + e) // 2
        self.mergesort(nums, s, m)
        self.mergesort(nums, m, e)
        self.merge(nums, s, m, e)

        return nums

    def firstMissingPositive(self, nums: List[int]) -> int:
        self.mergesort(nums, 0, len(nums)) # inplace
        # nums.sort()
        
        i = 0 # index of the first positive
        while i < len(nums) and nums[i] <= 0:
            i += 1

        if i == len(nums):
            return 1
        
        if nums[i] > 1:
            return 1

        # i on the first positive element
        # look for the gap
        for i in range(i, len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                return nums[i]+1
            
        return nums[-1] + 1


    def firstMissingPositiveSet(self, nums: List[int]) -> int:
        nums = set(nums)
        for num in range(1, 2**31-1):
            if num not in nums:
                return num

        return 2**31