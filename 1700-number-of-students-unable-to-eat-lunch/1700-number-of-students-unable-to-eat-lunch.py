class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        result=len(students)
        s={}
        for i in students:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        for j in sandwiches:
            if j in s and s[j]>0:
                result-=1
                s[j]-=1
            else:
                return result
        return 0
        


        