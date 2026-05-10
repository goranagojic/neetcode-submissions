class Solution:
    def removeDuplicatesOptimalButMoreComplex(self, nums: List[int]) -> int:
        # O(n) time complexity, O(1) extra space
        # Logic: when you see the same element, skip

        j, k = 0, len(nums) # assume all elements are unique
        for i in range(0,len(nums)-1):
            j = j + 1 # put j on the number after i
            while j < len(nums) and nums[i] == nums[j]: # it will stop when j is on the first diff value or j is out of bounds
                j += 1
                k -= 1
            
            if j >= len(nums):
                break

            nums[i+1] = nums[j] # logical delete
        
        return k

    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n) time complexity, O(1) space complexity
        # Logic: when you see different element write
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1

        return j


    def removeDuplicatesArray(self, nums: List[int]) -> int:
        tmp = [200] * len(nums)

        i = -1
        for num in nums:
            if num != tmp[i]:
                i += 1
                tmp[i] = num
            print(tmp)
            
        for j in range(0, len(tmp)):
            nums[j] = tmp[j]
        print(nums)

        return i+1

    def removeDuplicatesHashset(self, nums: List[int]) -> int:
        # with some extra space O(k), k - unique nums
        seen = set()
        
        j = 0
        for num in nums:
            if num in seen:
                continue
            nums[j] = num
            j += 1
            seen.add(num)
        
        return len(seen)