class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input: prices - always non-negative
        # return the maximum profit you can achieve (select one day to buy, and one day to sell)

        l, r = 0, 0
        max_profit = 0

        while l < len(prices) - 1: # because it is a different day

            if prices[l+1] <= prices[l]: # while the price is dropping, move l to buy on lower price
                l += 1
                continue

            r = l + 1 # this is the first moment the price starts to increse, buy on l
            best_sell = prices[r]
            while r < len(prices) and prices[r] > prices[l]:
                best_sell = max(best_sell, prices[r])
                r += 1

            print(f"l={l}, r={r-1}")
            max_profit = max(max_profit, best_sell - prices[l])
            l += 1

        return max_profit