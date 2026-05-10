class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # THE SIMPLIEST SOLUTION FOR NOW
        # Total time complexity: O(n+k) approximates to O(n)
        # Total space complexity: O(k), approximated with O(n) worstcase (when k=n-1)
        n = len(nums)
        if n == 0:
            return

        # 1. allocate helper list
        k = k % n 
        if k == 0:  # optimization, this condition helps avoid re-copying the same elements later in loop by early exit if no rotations are required
            return

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

    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        
        k = k % n
        if k == 0:
            return

        # 1) moves the last k elements to the first k elements in the reverse order
        for i in range(0, min(k, n//2)):
            t = nums[n-1-i]
            nums[n-1-i]=nums[i]
            nums[i]=t
        # print(f"1) nums = {nums}")

        # 2) reverses the first k elements
        for i in range(0, k // 2):
            t = nums[i]
            nums[i] = nums[k-1-i]
            nums[k-i-1] = t
        # print(f"2) nums = {nums}")

        # 3) reverse from k-end
        for i in range(0, (n-k) // 2 ):
            t = nums[k+i]
            nums[k+i] = nums[n-1-i]
            nums[n-1-i] = t
        # print(f"3) nums = {nums}")

        # 4) reverse 2k-end range (first 2k elems are in right place)
        if 2*k >= n:
            return
        for i in range(0, (n-2*k) // 2):
            t = nums[2*k+i]
            nums[2*k+i] = nums[n-1-i]
            nums[n-1-i] = t
        # print(f"4) nums = {nums}")

    def rotate(self, nums: List[int], k: int) -> None:
        # standard solution is
        n = len(nums)
        if n == 0:
            return
        
        k = k % n
        if k == 0:
            return

        # 1) reverse the whole array
        for i in range(0, n // 2):
            t = nums[n-1-i]
            nums[n-1-i] = nums[i]
            nums[i] = t

        # 2) reverse the first k elements
        for i in range(0, k // 2):
            t = nums[i]
            nums[i] = nums[k-1-i]
            nums[k-1-i] = t

        # 3) reverse the remaining n-k elements
        for i in range(0, (n-k)//2):
            t = nums[k+i]
            nums[k+i] = nums[n-1-i]
            nums[n-1-i]=t
