class Solution:
    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
        # time complexity O(n^3)
        # space complexity is O(r) for the output
        results = []
        # this loop O(n^3)
        for i in range(0, len(nums)-2):
            a = nums[i]
            for j in range(i+1, len(nums)-1):
                b = nums[j]
                for k in range(j+1, len(nums)):
                    c = nums[k]
                    if a + b + c == 0:
                        results.append(sorted([a, b, c])) # sort is of O(3log3) - const
        
        if len(results) == 0:
            return results

        j = 1
        results.sort()
        for i in range(1, len(results)): # O(rlogr) r - number of results, there will always be less then n solutions, so this is less then O(nlogn)
            if results[i] != results[i-1]:
                results[j] = results[i]
                j += 1

        return results[:j]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 0, len(nums) - 1

        results = set()
        for l in range(0, len(nums)-1):
            for r in range(len(nums)-1, -1, -1):
                if l >= r:
                    break
                lelem, relem = nums[l], nums[r]
                melem = 0 - lelem - relem
                if melem < 0:
                    # start searching from the left
                    m = l + 1
                    if m == r:
                        break
                    while m < r and melem > nums[m]: #melem != nums[m] and melem <= 0:
                        m += 1
                    if melem == nums[m]:
                        results.add(tuple([lelem, relem, melem]))
                else:
                    # start seraching from the right
                    m = r - 1
                    if m == l:
                        break
                    print(f"l={l} r={r} m={m}")
                    while m > l and melem < nums[m]: # and melem != nums[m] and melem >= 0:
                        m -= 1
                    if melem == nums[m]:
                        print(tuple([lelem, relem, melem]))
                        results.add(tuple([lelem, relem, melem]))

        return list(results)        


