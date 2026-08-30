class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculatesdays(weights,maxcapacity):
            day=1
            summ=0
            if sum(weights) < maxcapacity:
                day = 1
            for i in weights:
                if (summ+i)<=maxcapacity:
                    summ+=i
                else:
                    summ=i
                    day+=1
            return day
        m=max(weights)
        s=sum(weights)+1
        l=m
        r=s
        ans=0
        while l<=r:
            mid=(l+r)//2
            x=calculatesdays(weights,mid)
            if x<=days:
                ans=mid
            if x > days:
                l=mid+1
            else:
                r=mid-1
        return ans
                        