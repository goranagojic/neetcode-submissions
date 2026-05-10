class Solution:
    def getConcatenation1(self, nums: List[int]) -> List[int]:
        # in:  nums, len n
        # out: ans len 2n
        # time complexity: 2 * n * ~O(1), or avg. O(n). worstcase is 2 * n * O(m), O(nm)

        ans = []
        for i in range(0, 2):   # 2
            for num in nums:    # N
                ans.append(num) # ~O(1) (it can happen to be O(m) sometimes where m is the current sise of ans array)

        return ans

    def getConcatenation2(self, nums: List[int]) -> List[int]:
        # time complexity: O(n) (n accesses to the nums array, 2n to ans array)
        # same avg. and worst time complexity
        n = len(nums)
        # ans = [0] * 2 * n       # 2n, This option does allocation, but also incialization
        ans = [None] * 2 * n       # This option is actually faster because it just does allocation without inicialization
        for i in range(0, n):   # n * 2
            ans[i] = nums[i]    
            ans[i + n] = nums[i]

        return ans

    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums