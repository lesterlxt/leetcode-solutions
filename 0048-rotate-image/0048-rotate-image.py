class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left, right = 0, n - 1
        while left < right:
            for k in range(right - left):
                top, bottom = left, right
                tmp = matrix[top][left + k]
                matrix[top][left + k] = matrix[bottom - k][left]
                matrix[bottom - k][left] = matrix[bottom][right - k]
                matrix[bottom][right - k] = matrix[top + k][right]
                matrix[top + k][right] = tmp
            left += 1
            right -= 1

        