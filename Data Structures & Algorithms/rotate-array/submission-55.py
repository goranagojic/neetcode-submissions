class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # easy, not in-place
        if k == 0:
            return

        k = k % len(nums) # normalize

        # res = [0] * len(nums)

        # # copy the first k elements at the beggining
        # for i in range(0, k):
        #     res[i] = nums[len(nums) - k + i]

        # # copy the remaining elements
        # for i in range(0, len(nums) - k):
        #     res[k + i] = nums[i]

        
        # for i in range(0, len(nums)):
        #     nums[i] = res[i]

        # inplace

        n = len(nums)
        for i in range(0, k):
            # shift one place to the right
            t = nums[n-1]
            # print(t)
            for j in range(n-1, 0, -1):
                nums[j] = nums[j-1]
                # print(f"j -> {nums[j]}, j - 1 = {nums[j-1]}")
            nums[0] = t
        print(nums)


        # for i in range(0, k):
        #     t = nums[i]
        #     nums[i] = nums[n - k + i]
        #     nums[n - k + i] = t

        # if k < n // 2:
        #     # last k elems. shoud start from the index k in the array
            
        