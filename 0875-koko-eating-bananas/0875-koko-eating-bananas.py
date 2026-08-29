import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getans(y):
            sum=0
            for j in range(len(piles)):
                z=math.ceil(piles[j]/y)

                sum+=z
            return sum
        l=1
        r=max(piles)
        ans=0
        while l<=r:
            mid=(l+r)//2
            x=getans(mid)
            if x<=h:
                ans=mid
                r=mid-1
            else :
                l=mid+1
        return ans
    

                
                