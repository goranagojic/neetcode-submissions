class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        print(nums)
        j, k = 0, len(nums)
        for i in range(0,len(nums)-1):
            j = j + 1 # put j on the number after i
            while j < len(nums) and nums[i] == nums[j]: # while same move j
                j += 1
                k -= 1
            # it will stop when j is on the first diff value
            if j >= len(nums):
                break
            nums[i+1] = nums[j] # logical delete
            print(nums)
        
        return k