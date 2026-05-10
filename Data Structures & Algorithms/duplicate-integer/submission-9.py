class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     # hashset solution
    #     return len(nums) != len(set(nums))

    def hasDuplicate(self, nums: List[int]) -> bool:
        # bruteforce solution
        for i in range(len(nums)-1):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                if a == b:
                    return True
                
        return False

