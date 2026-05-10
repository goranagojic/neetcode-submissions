class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # total time complexity is O(n)
        # total space complexity: 
        freqs = [0, 0, 0]
        for num in nums: # t: O(n), s: O(1)
            freqs[num] += 1 # t: O(1)

        s = 0
        for i in range(0, len(freqs)): # s: O(1)
            val, freq = i, freqs[i]
            for j in range(0, freq):
                nums[s + j] = val
            s += freq

        