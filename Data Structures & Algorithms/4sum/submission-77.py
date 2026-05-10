class Solution:
    def fourSumIterativeOptimal(self, nums: List[int], target: int) -> List[List[int]]:
        # THIS IS OPTIMAL ITERATIVE SOLUTION FOR 4SUM CALCULATION IN O(N^3 time)

        nums.sort()

        results = []
        for fi in range(0, len(nums)-3):
            a = nums[fi]
            if fi > 0 and a == nums[fi-1]: # current number on fj pos is duplicate, already tested
                continue

            # min-max early exit/skip
            min_sum = a + nums[fi+1] + nums[fi+2] + nums[fi+3]
            if min_sum > target:
                break   # because min_sum cannot get smaller
            max_sum = a + nums[-3] + nums[-2] + nums[-1]
            if max_sum < target:
                continue # because max_sum can get larger

            for fj in range(fi+1, len(nums)-2):
                b = nums[fj]
                if fj > fi + 1 and b == nums[fj-1]: # current number on fj pos is duplicate, already tested
                    continue

                # min-max early exit/skip
                min_sum = a + b + nums[fj+1] + nums[fj+2]
                if min_sum > target:
                    break   # because min_sum cannot get smaller for this a, b combination
                max_sum = a + b + nums[-2] + nums[-1]
                if max_sum < target:
                    continue # because max_sum can grow in the subsequent iterations

                # the rest of the algorithm is this is standard 2sum on sorted array
                i, j = fj + 1, len(nums)-1
                while i < j:
                    s = a + b + nums[i] + nums[j]
                    if s == target:
                        results.append([a, b, nums[i], nums[j]])# NOTE previously, i had sorting here. it is redundant since searching pattern guarantees that fi < fj < i < j
                                                                # NOTE also, i used a set here, but with all skip duplicates conditions implemented the set is not needed
                        i, j = i + 1, j - 1
                        while i < j and nums[i] == nums[i-1]:   # skip duplicates, move i pointer until the next value is the same as the value you've just checked
                            i += 1
                        while i < j and nums[j] == nums[j+1]:   # skip duplicates, move j pointer until the next value is the same as the value you've just checked
                            j -= 1
                    elif s < target:
                        i += 1
                    else: # s > target
                        j -= 1

        return [list(r) for r in results]

    
    def fourSumBasic(self, nums: List[int], target: int) -> List[List[int]]:
        # BASIC RECURSIVE IMPLEMENTATION WITHOUT DUPLICATE CHECKING, JUST DUPLICATE FILTERING

        def twoSum(nums: List[int], s, e, quadruplet, target):
            i, j = s, e - 1
            results = set()
            while i < j: 
                quad_sum = sum(quadruplet) + nums[i] + nums[j]
                if quad_sum == target:
                    results.add(tuple(quadruplet + [nums[i]] + [nums[j]]))
                    i, j = i + 1, j - 1
                elif quad_sum < target:
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


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # BASIC RECURSIVE IMPLEMENTATION WITh DUPLICATE SKIPPING

        def twoSum(nums: List[int], s, e, quadruplet, target):
            i, j = s, e - 1
            results = list()
            while i < j: 
                quad_sum = sum(quadruplet) + nums[i] + nums[j]
                if quad_sum == target:
                    results.append(quadruplet + [nums[i], nums[j]])
                    i, j = i + 1, j - 1
                    # NOTICE this part skips duplicates, has to be separated to detect the same quadruplets when nums[i] or nums[j] repeats
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif quad_sum < target: 
                    # 1) skip adjusent equal values for i and j that do not lead to match, this is potential optimization when having multiple same values
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                else: # s > target
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1

            return list(results)

        def nSum(nums: List[int], s, e, quadruplet, target, k):

            results = []
            
            quadruplet_sum = sum(quadruplet)
            if k > 2:
                if quadruplet_sum + sum(nums[e-k:e]) < target:
                    return results

                for i in range(s, e-k+1):
                    # CHANGED: skip duplicates at this recursion depth (prevents duplicate quadruplets)
                    if i > s and nums[i] == nums[i - 1]:
                        continue

                    # min sum optimization condition
                    min_sum = quadruplet_sum + sum(nums[i:i+k])
                    if min_sum > target:
                        break

                    quadruplet.append(nums[i])
                    results.extend(nSum(nums, i+1, e, quadruplet, target, k - 1))
                    quadruplet.pop()
            elif k == 2:
                results = twoSum(nums, s, e, quadruplet, target)

            return results


        # MAIN
        # sort the array
        nums.sort()
        return nSum(nums, 0, len(nums), [], target, 4)