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

    def sortArray(self, nums: List[int]) -> List[int]:
        # constraints: minimal space complexity, O(nlogn) time complexity
        # so, time complexity is satisfied O(nlogn), but space complexity is not (it is O(n) for result array)

        heapq.heapify(nums) # t: O(n)
        i = len(nums)
        result = list()
        while i: # n iterations, this complete loop is O(nlogn)
            result.append(heapq.heappop(nums)) # O(log n)
            i -= 1
        
        return result

    

        