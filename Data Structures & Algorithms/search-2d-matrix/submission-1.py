class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0

        rows = len(matrix)
        columns = len(matrix[0])

        right = rows * columns - 1

        while left <= right:
            index = (left + right) // 2

            row = index // columns
            column = index % columns

            value = matrix[row][column]

            if value == target:
                return True
            elif target > value:
                left = index + 1
            else:
                right = index - 1

        return False