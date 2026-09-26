from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q=deque()
        result=[]
        for i in range(len(nums)):
            if q and i-q[0] >= k:
                q.popleft()
            while len(q)!=0 and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                result.append(nums[q[0]])
        return result
