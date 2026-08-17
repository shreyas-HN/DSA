class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        maxi=0
        l=0
        r=n-1
        while l<r:
            width=r-l
            area=width*min(height[l],height[r])
            maxi=max(area,maxi)
            if height[l]<height[r]:
                l+=1
            elif height[l]==height[r]:
                l+=1
            else:
                r-=1
        return maxi