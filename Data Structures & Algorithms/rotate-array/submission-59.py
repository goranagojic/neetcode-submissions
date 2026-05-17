class Solution:
    def rotate(self, nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        # easy, not in-place
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




    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # # inplace
        # # The main idea: implement one-place right shift, repeat it k times.
        # n = len(nums)
        # # time complexity: O(k*n) where k is shift factor and n is the array length
        # # in worst case k coult be n/2 with time complexity being O(n/2*n) approximated to O(n2)
        # # if k > n/2 you could do the left shift with n-k factor that will be more efficient than right shift with the same result
        # for i in range(0, k):
        #     # shift one place to the right
        #     t = nums[n-1]
        #     for j in range(n-1, 0, -1):
        #         nums[j] = nums[j-1]
        #     nums[0] = t
        # print(nums)


        # reverse array inplace
        def reverse(nums: List[int], s, e):
            i, j = s, e - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1


        # reverse the whole array
        reverse(nums, 0, len(nums))

        # reverse the first k
        reverse(nums, 0, k)

        # reverse the last n - k elements
        reverse(nums, k, len(nums))
            
        