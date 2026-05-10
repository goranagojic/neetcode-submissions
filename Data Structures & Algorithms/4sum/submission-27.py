class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        results = set()
        for fi in range(0, len(nums)-3):
            a = nums[fi]
            for fj in range(fi+1, len(nums)-2):
                b = nums[fj]
                i, j = fj+1, len(nums)-1
                while i < j:
                    s = a + b + nums[i] + nums[j]
                    if s == target:
                        r = [a, b, nums[i], nums[j]]
                        results.add(tuple(r))
                        i += 1
                        j -= 1
                    elif s < target:
                        i += 1
                    else: # s > target
                        j -= 1

        return list(results)