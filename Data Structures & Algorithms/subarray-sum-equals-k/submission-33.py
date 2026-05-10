class Solution:
    def subarraySum1(self, nums: List[int], k: int) -> int:

        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i] # i ovo moze da se izbaci tako sto ce se koristiti samo trenutna suma

        cnts = {0 : 1}
        result = 0
        for prefix in nums:
            if prefix - k in cnts:
                result += cnts[prefix - k]
            
            cnts[prefix] = cnts.get(prefix, 0) + 1

        return result


    def subarraySum(self, nums: List[int], k: int) -> int:

        cnts = {0 : 1}
        prefixSum, result = 0, 0
        for i in range(0, len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in cnts:
                result += cnts[prefixSum - k]
            
            cnts[prefixSum] = cnts.get(prefixSum, 0) + 1

        return result
        