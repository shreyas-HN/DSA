class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=1
        r=len(nums)-2
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        while l<=r:
            mid=(l+r)//2
            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if nums[mid] == nums[mid - 1]:
                if mid % 2 == 1:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if mid % 2 == 0:
                    l = mid + 1
                else:
                    r = mid - 1
