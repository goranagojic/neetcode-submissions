import heapq

class Solution:
    def sortArrayBubbleSort(self, nums: List[int]) -> List[int]:
        # brute force solution O(n^2)
        # bubble sort algorithm
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

    def sortArrayHeapsort(self, nums: List[int]) -> List[int]:
        # constraints: minimal space complexity, O(nlogn) time complexity
        # so, time complexity is satisfied O(nlogn), but space complexity is not (it is O(n) for result array)
        # but i use a built-in function which is not allowed, nah

        heapq.heapify(nums) # t: O(n)
        i = len(nums)
        result = list()
        while i: # n iterations, this complete loop is O(nlogn)
            result.append(heapq.heappop(nums)) # O(log n)
            i -= 1
        
        return result

    def sortArrayBucketSort(self, nums: List[int]) -> List[int]:
        pass

    def sortArrayCountSort(self, nums: List[int]) -> List[int]:
        pass

    def _conquer(self, nums: List[int], s: int, m: int, e: int, result: List[int]):
        # ln, rn = len(left), len(right)
        ln, rn = m - s, e - m
        li, ri = 0, 0

        for i in range(s,e):
            # are there elements in both partitions
            if li < ln and ri < rn:
                # print(f"sli {s+li}, mri {m+ri}")
                if nums[s+li] <= nums[m+ri]:
                    result[i] = nums[s+li]
                    li += 1
                else:
                    result[i] = nums[m+ri]
                    ri += 1
            elif li < ln:
                result[i] = nums[s+li]
                li += 1
            else:
                result[i] = nums[m+ri]
                ri += 1

        # copy to original array
        nums[s:e] = result[s:e]
            

    def _mergesort(self, nums: List[int], s, e, buffer):
        # sorts nums[s:e] and returns a NEW sorted list
        if e - s <= 1:
            return  # length 0 or 1

        # split - divide
        m = s + (e - s) // 2
        # print(f"len nums: {len(nums)}, m={m}")
        self._mergesort(nums, s, m, buffer)
        # print(f"divided to {left} on :{m}")
        self._mergesort(nums, m, e, buffer)
        # print(f"divided to {right} on m {m}:")
        # return self._conquer(left, right)
        self._conquer(nums, s, m, e, buffer)
        # print(f"conquer {left} {right} got {tmp}")
        


    def sortArray(self, nums: List[int]) -> List[int]: # merge sort
        buffer = [0] * len(nums)
        self._mergesort(nums, 0, len(nums), buffer)

        return nums
