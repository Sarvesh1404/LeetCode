class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=math.inf
        sell=0
        for price in prices:
            profit=price-buy
            sell=max(sell,profit)
            buy=min(buy,price)
        return sell