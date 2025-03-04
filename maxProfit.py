class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,max_profit = 0,0
        while low < len(prices) -1:
            remaining_list = prices[low+1:]
            max_val = max(remaining_list)
            profit = max_val - prices[low]
            if profit > max_profit:
                max_profit = profit
            low+=1
        return max_profit
