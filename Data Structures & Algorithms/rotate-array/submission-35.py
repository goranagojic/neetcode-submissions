class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k == 0:
            return

        k = k % len(nums) # normalize

        res = [0] * len(nums)

        # copy the first k elements at the beggining
        for i in range(0, k):
            res[i] = nums[len(nums) - k + i]

        # copy the remaining elements
        for i in range(0, len(nums) - k):
            res[k + i] = nums[i]

        
        for i in range(0, len(nums)):
            nums[i] = res[i]