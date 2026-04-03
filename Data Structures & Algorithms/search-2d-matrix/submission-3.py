class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bottom = len(matrix) - 1

        row = -1

        while top <= bottom:

            row = (top + bottom) // 2
            if matrix[row][0] <= target <= matrix[row][COLS - 1]:
                break
            
            if target > matrix[row][COLS - 1]:
                top += 1
            else:
                bottom -= 1
        
        if not (top<=bottom):
            return False
        

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:

            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            
            if target > matrix[row][mid]:
                l += 1
            else:
                r -= 1
        
        return False











        
