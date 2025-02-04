class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_in = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_in > p:
                buy_in = p
            
            profit = max(profit, p - buy_in)
        
        return profit
