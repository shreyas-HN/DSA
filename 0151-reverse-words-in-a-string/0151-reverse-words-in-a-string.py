class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split()
        i=0
        j=len(li)-1
        while i<j:
            li[i],li[j]=li[j],li[i]
            i+=1
            j-=1
        x=" ".join(li)
        return x
                