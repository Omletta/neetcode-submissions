class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        area = 0
        def dfs(r,c):

            nonlocal area
            if (r<0 or c <0 or r >= rows or c >= cols or grid[r][c] == 0 ):
                return
            
            grid[r][c] = 0
            area +=1 

            for dr,dc in directions :
                nr = dr + r
                nc = dc + c 

                dfs(nr,nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    max_area = max(max_area,area)

        return max_area



            