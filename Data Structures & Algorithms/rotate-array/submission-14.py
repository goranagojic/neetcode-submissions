class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # the simpliest solution for now

        # 1. allocate helper list
        n = len(nums)
        if k > n:
            k = k % n

        tmp = [0] * k

        # 2. copy the last k elements to the helper list
        for i in range(0,k):
            print(f"{i} - {n-k+i}")
            tmp[i] = nums[n-k+i]
        print(tmp)

        # 3. move the rest of the elements towards the end
        for i in range(n-k-1, -1, -1):
            # print(i)
            nums[i+k] = nums[i]
        print(nums)

        # 4. copy-back from helper list to the original array
        for i in range(0, len(tmp)):
            nums[i] = tmp[i]
        print(nums)