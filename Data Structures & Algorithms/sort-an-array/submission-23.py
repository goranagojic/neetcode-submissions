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

    def _conquer(self, left: List[int], right: List[int]) -> List[int]:

        # ne valja

        ln, rn = len(left), len(right)
        li, ri = 0, 0
        result = [0] * (ln+rn)

        for i in range(0, len(result)):
            # are there elements in both partitions
            if li < ln and ri < rn:
                if left[li] < right[ri]:
                    result[i] = left[li]
                    li += 1
                else:
                    result[i] = right[ri]
                    ri += 1
            elif li < ln:
                result[i] = left[li]
                li += 1
            else:
                result[i] = right[ri]
                ri += 1

        return result
            

    def _mergesort(self, nums: List[int]) -> List[int]:
        tmp = nums
        if len(nums) not in [0,1]:
            # split - divide
            m = len(nums) // 2
            # print(f"len nums: {len(nums)}, m={m}")
            left = self._mergesort(nums[:m])
            # print(f"devided to {left} on :{m}")
            right = self._mergesort(nums[m:])
            # print(f"divided to {right} on m {m}:")
            tmp = self._conquer(left, right)
            # print(f"conquer {left} {right} got {tmp}")
        # merge
        return tmp


    def sortArray(self, nums: List[int]) -> List[int]: # merge sort
        return self._mergesort(nums)
