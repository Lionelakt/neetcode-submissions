class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_valid(i,j):
            return ( 
            0 <= i < rows 
            and 0 <= j < cols
            and grid[i][j] == 1
            and (not (i,j) in visited))


        
        def dfs_iterative(start):
            visited = set()
            stack = [start]
            nonlocal max_area
            while stack:
                (x,y) = stack.pop()
                if (x,y) not in visited:
                    visited.add((x,y))
                    max_area += 1
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if is_valid(nx,ny):
                            stack.append((nx,ny))
            

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        max_area = 0
        best = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                #and not (i,j) in visited:
                    dfs_iterative((i,j))
                    if best < max_area:
                        best = max_area
                    max_area = 0
        return best

                    


        
        



        
        



