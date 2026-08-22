class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        product=1
        temp=n
        while n>0:
            digit=n%10
            sum+=digit
            product*=digit
            n=n//10
        if temp%(sum+product)==0:
            return True
        else:
            return False
    