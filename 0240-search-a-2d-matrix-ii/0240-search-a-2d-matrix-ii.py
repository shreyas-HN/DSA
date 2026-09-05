class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        i=0
        j=n-1
        while m>i>=0 and 0<=j<=n-1:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                j-=1
            elif matrix[i][j]<target:
                i+=1
        return False
        