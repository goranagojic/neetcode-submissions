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

                


    # def maxProfit(self, prices: List[int]) -> int:

    #     min_prices = [(price, index) for index, price in enumerate(prices)]
    #     heapq.heapify(min_prices)

    #     max_prices = [(-price, index) for index, price in enumerate(prices)]
    #     heapq.heapify(max_prices)

    #     max_profit = 0
    #     min_price, max_price = heapq.heappop(min_prices), heapq.heappop(max_prices)
    #     while len(min_prices) and len(max_prices):
    #         min_price_idx, max_price_idx = min_price[1], max_price[1]
    #         min_price_val, max_price_val = min_price[0], -max_price[0]
    #         print(f"{max_price_idx}, {max_price_val} - {min_price_idx}, {min_price_val}")
    #         # break

    #         if min_price_idx > max_price_idx:
    #             min_price = heapq.heappop(min_prices)
    #         else:
    #             profit = max_price_val - min_price_val
    #             max_profit = max(max_profit, profit)
    #             max_price = heapq.heappop(max_prices)

    #     if max_profit < 0:
    #         return 0

    #     return max_profit

        