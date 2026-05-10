class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        sell_price = prices[0]
        for price in prices[1:]:
            if price > sell_price:
                sell_price = price
            elif price == sell_price:
                continue
            else:
                if sell_price > buy_price:
                    profit += sell_price - buy_price
                buy_price = price
                sell_price = price

        if sell_price > buy_price:
            profit += sell_price - buy_price

        return profit