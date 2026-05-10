class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """ 
        # time complexity of the solution: O(m) to move elements of num1 to the end, then O(m) + O(n) to iterate through nums1 and nums2 arrays
        # total time complexity is O(n+m)
        # Space complexity depends on the implementation
        # if using while loops for that remaining elemennt assignment, it is O(1)
        # if using slicing, it is O(k) where the K is the slice length
        # slicing version is faster comparing to loop version because it is usually implemented in cpython which is faster
        # move elements in num1 to the end (from the last to the first element)
        for i in range(m-1,-1,-1):
            nums1[n+i] = nums1[i]

        # merge in non-decreasing order, keeps stability
        i, j, r = n, 0, 0
        while i < n+m and j < n:
            if nums1[i] <= nums2[j]:
                nums1[r] = nums1[i]
                i += 1
            else:
                nums1[r] = nums2[j]
                j += 1
            r += 1

        # more time efficient, less memory efficient (space complexity O(k))
        if i < n+m:
            nums1[r:] = nums1[i:]
        if j < n:
            nums1[r:] = nums2[j:] 

        # Better space complexity O(1), slower than slicing because slicing is usually implemented in cython
        # while i < n+m:
        #     nums1[r] = nums1[i]
        #     i += 1
        #     r += 1

        # while j < n:
        #     nums1[r] = nums2[j]
        #     j += 1
        #     r += 1

