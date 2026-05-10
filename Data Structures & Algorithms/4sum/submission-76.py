class Solution:
    # basic recursive implementation
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def twoSum(nums: List[int], s, e, quadruplet, target):
            i, j = s, e - 1
            results = set()
            while i < j: 
                s = sum(quadruplet) + nums[i] + nums[j]
                if s == target:
                    results.add(tuple(quadruplet + [nums[i]] + [nums[j]]))
                    i, j = i + 1, j - 1
                elif s < target:
                    i += 1
                else: # s > target
                    j -= 1

            return list(results)

        def nSum(nums: List[int], s, e, quadruplet, target, k):

            results = list()
            
            if k > 2:
                for i in range(s, e-k+1):
                    quadruplet.append(nums[i])
                    results.extend(nSum(nums, i+1, e, quadruplet, target, k - 1))
                    quadruplet.pop()
            elif k == 2:
                results = twoSum(nums, s, e, quadruplet, target)

            return list(set(results))


        # MAIN
        # sort the array
        nums.sort()
        return nSum(nums, 0, len(nums), [], target, 4)

        
        