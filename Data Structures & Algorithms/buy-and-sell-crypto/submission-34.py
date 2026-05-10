import heapq

class Solution:
    # desired solution
    # time complexity - O(n)
    # space complexity - O(1)

    def maxProfitBruteForce(self, prices: List[int]) -> int:
        # O(n^2) time complexity
        max_profit, profit = 0, 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(prices[j] - prices[i], profit)
            max_profit = max(profit, max_profit)

        return max_profit

    def maxProfit(self, prices: List[int]):
        # sliding window algorithm
        # time complexity O(n) - single pass
        # space complexity - O(1) - two pointers, constant size
        if not prices or len(prices) == 0:
            return 0

        buy, sell, max_profit = 0, 1, 0
        while sell < len(prices):
            if prices[buy] <= prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1

        return max_profit
        