class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # move elements
        print(f"1. {nums1}")
        for i in range(m-1,-1,-1):
            nums1[n+i] = nums1[i]
        print(f"2. {nums1}")

        # merge
        i, j, r = n, 0, 0
        while i < n+m and j < n:
            if nums1[i] <= nums2[j]:
                nums1[r] = nums1[i]
                i += 1
            else:
                nums1[r] = nums2[j]
                j += 1
            r += 1

        print(f"3. {nums1}")

        while i < n+m:
            nums1[r] = nums1[i]
            i += 1
            r += 1
        print(f"4. {nums1}")

        while j < n:
            nums1[r] = nums2[j]
            j += 1
            r += 1
        print(f"5. {nums1}")

