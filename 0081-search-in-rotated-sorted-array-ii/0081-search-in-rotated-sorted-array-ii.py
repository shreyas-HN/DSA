class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        f=False 
        if target in set(nums):
            f=True
        return f
        