class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # THE SIMPLIEST SOLUTION FOR NOW
        n = len(nums)
        if n == 0:
            return []

        if k == 0:
            return nums

        # 1. allocate helper list
        if k > n:
            k = k % n

        tmp = [0] * k

        # 2. copy the last k elements to the helper list
        for i in range(0,k):
            tmp[i] = nums[n-k+i]

        # 3. move the rest of the elements towards the end
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]

        # 4. copy-back from helper list to the original array
        for i in range(0, len(tmp)):
            nums[i] = tmp[i]