class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        lines = len(matrix)
        columns = len(matrix[0])

        right = lines * columns 

        while left <= right :
            r_index =(( right + left) // 2) 

            r_line = (r_index // columns) -1 
            r_column =(r_index % columns ) - 1

            if matrix[r_line][r_column] == target:
                return True
            elif target > matrix[r_line][r_column]:
                left = r_index + 1 
            else:
                right = r_index - 1

        return False
        
       