class Solution:
    def find_next_valid(self,string,i):
        skip=0
        while i>=0:
            if string[i]=="#" :
                skip+=1
                i-=1
            elif skip>0:
                i-=1
                skip-=1
            else:
                return i
        return i
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        while i>=0 or j>=0:
            x=self.find_next_valid(s,i)
            y=self.find_next_valid(t,j)
            if x ==-1 and y==-1:
                return True
            if x==-1 or y==-1:
                return False
            if s[x]!=t[y]:
                return False
            i=x-1
            j=y-1
        return True
            