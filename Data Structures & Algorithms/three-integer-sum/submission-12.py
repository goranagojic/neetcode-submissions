class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        for i in range(0, len(nums)-2):
            a = nums[i]
            for j in range(i+1, len(nums)-1):
                b = nums[j]
                for k in range(j+1, len(nums)):
                    c = nums[k]
                    if a + b + c == 0:
                        results.append(sorted([a, b, c]))
        
        if len(results) == 0:
            return results

        j = 1
        results.sort()
        for i in range(1, len(results)):
            if set(results[i]) != set(results[i-1]):
                results[j] = results[i]
                j += 1

        return results[:j]

