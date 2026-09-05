class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def getmax(mat, col):
            max_row = 0

            for row in range(1, len(mat)):
                if mat[row][col] > mat[max_row][col]:
                    max_row = row

            return max_row

        rows = len(mat)
        cols = len(mat[0])

        l = 0
        r = cols - 1

        while l <= r:
            mid = (l + r) // 2

            row = getmax(mat, mid)
            current = mat[row][mid]

            left = mat[row][mid - 1] if mid > 0 else -1
            right = mat[row][mid + 1] if mid < cols - 1 else -1

            if current > left and current > right:
                return [row, mid]

            if left > current:
                r = mid - 1
            else:
                l = mid + 1

        return [-1, -1]