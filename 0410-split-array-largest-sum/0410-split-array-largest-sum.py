class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splitter(nums,maxsum):
            count=1
            summ=0
            for i in nums:
                if (summ+i) > maxsum:
                    count+=1
                    summ=0
                summ+=i

            return count
        l=max(nums)
        r=sum(nums)
        answer=0
        while l<=r:
            mid=(l+r)//2
            x=splitter(nums,mid)
            print(x)
            if x<=k:
                answer=mid
                r = mid - 1
            elif x>k:
                l=mid+1

        return answer
        