class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        ans=prices.copy()
        for i in range(len(prices)):
            while len(stack)!=0 and prices[i]<=prices[stack[-1]]:
                z=stack.pop()
                price=prices[z]-prices[i]
                ans[z]=price
            stack.append(i)
        return ans
                