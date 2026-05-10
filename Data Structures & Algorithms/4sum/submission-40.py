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
                
                # the rest of the algorithm is this is standard 2sum on sorted array
                i = fj+1
                c = nums[i]
                if i > fj+1 and c == nums[i-1]:        # skip checking the same value for i, already tested - boundary checks are important!
                    i += 1
                    continue

                j = len(nums)-1
                d = nums[j]
                if j < len(nums)-1 and d == nums[j+1]: # skip checking the same value for j, already tested - boundary checks are important!
                    j -= 1
                    continue

                while i < j:
                    c, d = nums[i], nums[j]
                    s = a + b + c + d
                    if s == target:
                        r = [a, b, c, d]
                        results.add(tuple(r)) # previously, i had sorting here 
                        i, j = i + 1, j - 1
                    elif s < target:
                        i += 1
                    else: # s > target
                        j -= 1

        return list(results)