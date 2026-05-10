class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        print(nums)
        j, k = 0, len(nums)
        for i in range(0,len(nums)-1):
            j = j + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
                k -= 1
            # it will stop when j is on the first diff value
            print(f"i={i},j={j}")
            if j >= len(nums):
                break
            nums[i+1] = nums[j]
            print(nums)
        
        return k