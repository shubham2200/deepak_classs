class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        min_value = 1e9
        profit = -1e9
        for i in range(len(p)):
            min_value = min(min_value, p[i])
            print(min_value,'ascasc')
            profit = max(profit, p[i] - min_value)

        return profit
