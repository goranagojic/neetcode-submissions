class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        results = []
        for fi in range(0, len(nums)-3):
            a = nums[fi]
            if fi > 0 and a == nums[fi-1]: # current number on fj pos is duplicate, already tested
                continue

            for fj in range(fi+1, len(nums)-2):
                b = nums[fj]
                if fj > fi + 1 and b == nums[fj-1]: # current number on fj pos is duplicate, already tested
                    continue

                # the rest of the algorithm is this is standard 2sum on sorted array
                i, j = fj + 1, len(nums)-1

                min_sum = a + b + nums[i] + nums[i+1]
                max_sum = a + b + nums[j] + nums[j-1]

                if target < min_sum: # there will be no match for this a, b because min_sum cannot be smaller (a+b+two smallest remaining elements)
                    break

                if target > max_sum: # similarly, there will be no match for this a, b if a+b+two maximal elements are still smaller then target
                    continue

                while i < j:
                    s = a + b + nums[i] + nums[j]
                    if s == target:
                        r = [a, b, nums[i], nums[j]]
                        results.append(tuple(r))                # NOTE previously, i had sorting here. it is redundant since searching pattern guarantees that fi < fj < i < j
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