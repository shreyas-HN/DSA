class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        maxprofit=0
        for j in range(len(prices)):
            if prices[j]<min_price:
                min_price=prices[j]
            profit=prices[j]-min_price
            maxprofit=max(profit,maxprofit)
        return maxprofit

        