class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
    
        j, k = 0, len(nums)
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