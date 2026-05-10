class Solution:
    def longestConsecutiveBruteForce(self, nums: List[int]) -> int:
        # brute-force solution
        if not nums:
            return 0

        if len(nums) == 0:
            return 0

        max_cnt = 1

        # time complexity of this solution is O(n*m) where n is number of elements, and m is avg. seq. length for all elem
        # the worst case for this alg when sequence can be formed for each elem. e.g. 0, 1, 2, 3, ...
        # so that m is n, then n-1, then n-2, etc. n(n-1)/2. in that case O(n) * O(n^2) = O(n^3)
        store = set(nums)
        for num in nums: # O(n)
            next_num, cnt = num + 1, 1         # repeat the check if the next elem. is in nums,
            while next_num in store: # O(m*1)  # keep repeating and counting until there is no next elem
                cnt += 1
                next_num = next_num + 1

            max_cnt = max(max_cnt, cnt)         # then you've found the sequence, check if it is the longest seen

            print(f"new max seq length is {max_cnt}")
                
        return max_cnt

    def longestConsecutiveSorting(self, nums: List[int]) -> int:
        # total time complexity is O(nlogn)

        if not nums:
            return 0

        if len(nums) == 0:
            return 0

        nums.sort() #O(nlogn)
        max_cnt, cnt, prev = 1, 1, nums[0]
        for num in nums[1:]: # O(n)
            if num == prev:
                continue

            if num == prev + 1:
                cnt += 1
            else:
                max_cnt, cnt = max(max_cnt, cnt), 1
            prev = num

        max_cnt = max(max_cnt, cnt)

        return max_cnt

    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums or len(nums) == 0:
            return 0

        # init lognest seq, and seq cnt
        max_cnt, cnt = 1, 1

        # use hashset for quick lookup
        store = set(nums)

        for num in nums:
            # check if num is start of the sequence
            if (num - 1) in store:
                continue # if no, just proceed to the next num

            # if yes, start generating the rest of the seq and counting
            next_num = num + 1
            while next_num in store:
                cnt += 1
                next_num += 1
            max_cnt, cnt = max(cnt, max_cnt), 1

        return max_cnt

            
        