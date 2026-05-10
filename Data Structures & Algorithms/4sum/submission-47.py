class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        results = []
        for fi in range(0, len(nums)-3):
            a = nums[fi]
            if fi > 0 and a == nums[fi-1]: # current number on fj pos is duplicate, already tested
                continue

            # min-max early exit/skip
            min_sum = a + nums[fi+1] + nums[fi+2] + nums[fi+2]
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