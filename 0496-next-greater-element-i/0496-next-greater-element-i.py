class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[nums2[0]]
        dictans={}
        for num in nums2:
            if num < stack[-1]:
                stack.append(num)
            else:
                while len(stack) != 0 and num > stack[-1]:
                    z = stack.pop()
                    dictans[z]=num
                stack.append(num)
        for i in stack:
            dictans[i]=-1
        ans=[]
        for j in nums1:
            ans.append(dictans[j])
        return ans