class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        pref=[0]*n
        pref[0]=nums[0]
        for k in range(1,n):
            pref[k]=pref[k-1]+nums[k]
        d=dict()
        j=0
        d[0]=-1
        maxi=0
        while j<n:
            if pref[j] in d:
                diff=j-d[pref[j]]
                maxi=max(maxi,diff)
            if pref[j] not in d:
                d[pref[j]]=j
            j+=1
        return maxi
            


        