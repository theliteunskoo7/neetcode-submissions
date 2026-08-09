class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy=0
        op=0
        for i in range(1,n):
            sell = prices[i]-prices[buy]
            op=max(op,sell)
            if prices[i]<prices[buy]:
                buy=i
        return op
