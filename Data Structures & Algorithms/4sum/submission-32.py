class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        results = set()
        for fi in range(0, len(nums)-3):
            a = nums[fi]

            if fi > 0 and a == nums[fi-1]: # current number on fj pos is duplicate, already tested
                continue

            for fj in range(fi+1, len(nums)-2):
                b = nums[fj]

                if fj > fi + 1 and b == nums[fj-1]: # current number on fj pos is duplicate, already tested
                    continue
                
                # this is standard 2sum on sorted array
                i, j = fj+1, len(nums)-1
                while i < j:
                    s = a + b + nums[i] + nums[j]
                    if s == target:
                        r = [a, b, nums[i], nums[j]]
                        results.add(tuple(r)) # previously, i had sorting here 
                        i += 1
                        j -= 1
                    elif s < target:
                        i += 1
                    else: # s > target
                        j -= 1

        return list(results)