class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_valid(i,j):
            return ( 
            0 <= i < rows 
            and 0 <= j < cols
            and grid[i][j] == 1)
            #and (not (i,j) in visited))

        def dfs(node):
            grid[node[0]][node[1]] = 0
            #visited.add(node)
            nonlocal max_area
            max_area += 1
            for di, dj in dirs:
                ni, nj = node[0] + di, node[1] +dj
                if is_valid(ni, nj):
                    dfs((ni,nj))
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        #visited = set()
        max_area = 0
        best = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                #and not (i,j) in visited:
                    dfs((i,j))
                    if best < max_area:
                        best = max_area
                    max_area = 0
        return best

                    


        
        



        
        



