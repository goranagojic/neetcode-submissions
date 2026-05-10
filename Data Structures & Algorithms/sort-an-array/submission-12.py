import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # brute force solution O(n^2)
        # bubble sort algorithm
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        # constraints: minimal space complexity, O(nlogn) time complexity
        heapq.heapify(nums)
        i = len(nums)
        result = list()
        while i:
            result.append(heapq.heappop(nums))
            i -= 1
        
        return result

    

        