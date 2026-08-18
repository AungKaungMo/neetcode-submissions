class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_row, mid_col = mid // COLS, mid % COLS

            if matrix[mid_row][mid_col] < target:
                l = mid + 1
            elif matrix[mid_row][mid_col] > target:
                r = mid - 1
            else:
                return True
        
        return False





