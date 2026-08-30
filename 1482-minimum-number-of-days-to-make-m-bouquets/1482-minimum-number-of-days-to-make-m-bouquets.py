class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def numberofbouquets(bloomDay,day,k):
            count=0
            b = 0
            for i in bloomDay:
                if day>=i:
                    b+=1
                else:
                    b=0
                    continue
                if b==k:
                    count+=1
                    b=0
            return count
        l=min(bloomDay)
        r=max(bloomDay)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            x=numberofbouquets(bloomDay,mid,k)
            if x<m:
                l=mid+1
            else:
                r=mid-1
            if x>=m:
                ans=mid
        return ans
            