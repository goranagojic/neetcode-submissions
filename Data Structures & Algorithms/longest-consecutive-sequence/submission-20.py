class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute-force solution
        if not nums:
            return 0

        if len(nums) == 0:
            return 0

        max_cnt, cnt = 1, 1

        store = set(nums)
        for num in nums:
            next_num = num + 1          # repeat the check if the next elem. is in nums
            while next_num in store:    # keep repeating and counting until there is no next elem
                cnt += 1
                next_num = next_num + 1

            max_cnt = max(max_cnt, cnt) # then you've found the sequence, check if it is the longest seen
            cnt = 1                     # and reset the counter for the new seq length count

            print(f"new max seq length is {max_cnt}")
                
        return max_cnt
        