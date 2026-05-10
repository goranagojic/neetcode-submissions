class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Return the length of the longest consecutive sequence.
        # Time:  O(n) average. Each element is visited at most twice across the whole
        #        algorithm — once by the outer loop's predecessor check, once by the
        #        inner while-loop walk of its sequence. Total work is therefore bounded
        #        by 2n, giving O(1) amortized per outer iteration.
        #        Worst case is O(n^2) only under adversarial hash collisions in `set`.
        # Space: O(n) for the set.

        if not nums:
            return 0

        num_set = set(nums)                  # O(n) build
        longest = 0

        for start in num_set:                # n iterations (deduped)
            if start - 1 in num_set:         # O(1) average; skip non-starts
                continue

            current, length = start + 1, 1
            while current in num_set:        # O(1) average per check; total
                length += 1                  # checks across all walks <= n
                current += 1

            longest = max(longest, length)

        return longest