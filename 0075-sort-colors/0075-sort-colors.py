class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n=len(nums)
        left=0
        right=n-1
        middle=0
        if n==1:
            return nums
        while middle<=right:
            if nums[middle]==2:
                nums[middle],nums[right]=nums[right],nums[middle]
                right-=1
            elif nums[middle]==1:
                middle+=1
            else:
                nums[middle],nums[left]=nums[left],nums[middle]
                left+=1
                middle+=1
        return nums

            
        