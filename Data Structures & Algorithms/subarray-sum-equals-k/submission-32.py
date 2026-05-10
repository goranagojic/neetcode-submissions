class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]

        cnts = {0 : 1}
        result = 0
        for prefix in nums:
            if prefix - k in cnts:
                result += cnts[prefix - k]
            
            cnts[prefix] = cnts.get(prefix, 0) + 1

        return result
        