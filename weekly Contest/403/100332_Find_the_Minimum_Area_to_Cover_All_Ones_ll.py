class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def minimumArea(grid: List[List[int]]) -> int:
            rows = len(grid)
            cols = len(grid[0])

            mr, xr = rows, -1
            mc, xc = cols, -1

            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        if i < mr:
                            mr = i
                        if i > xr:
                            xr = i
                        if j < mc:
                            mc = j
                        if j > xc:
                            xc = j

            h = xr - mr + 1
            w = xc - mc + 1

            return h * w
        
        grid1 = [[1,0,1],[1,1,1]]
        grid2 = [[1,0,1,0],[0,1,0,1]]

        print(minimumArea(grid1))
        print(minimumArea(grid2))
        
        return -1
      
#This solution for the question is not correct i amn only saving it to rechack later so dont use this and if you know ther correct feel free to update the file.
