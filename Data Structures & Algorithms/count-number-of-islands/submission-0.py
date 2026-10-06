class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        def bfs(r,c):

            if (r<0 or c <0 or r >=rows or c >= cols or grid[r][c] == "0" ):
                return 

            grid[r][c] = "0"

            for d in directions :

                nr = d[0]+r
                nc = d[1]+c

                bfs(nr,nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i,j)
                    islands +=1

            

        return islands





            