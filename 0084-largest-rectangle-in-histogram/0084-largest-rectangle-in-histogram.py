class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[]
        maxi=0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                z=stack.pop()
                if stack:
                    l=stack[-1]
                else:
                    l=-1
                right=i
                width=right-l-1
                area=heights[z]*width
                maxi=max(maxi,area)
            stack.append(i)
        return maxi