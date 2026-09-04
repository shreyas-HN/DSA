class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_place(position, distance, m):
            count=1
            last=position[0]
            for i in range(1,len(position)):
                if position[i]-last>=distance:
                    count+=1
                    last=position[i]
                else:
                    continue
                if count>=m:
                    return True
            return False
        answer=0
        l=1
        r=max(position)-min(position)
        position.sort()
        while l<=r:
            mid=(l+r)//2
            if can_place(position,mid, m):
                answer=mid
                l=mid+1
            else:
                r=mid-1
        return answer
            