class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        if len(s)==0:
            return 0
        i=len(s)-1
        while i>=0:
            if s[i].isalnum():
                count+=1
                i-=1
            elif (not s[i].isalnum()) and (count==0):
                i-=1
            elif (not s[i].isalnum()) and (count>0):
                break
        return count
            