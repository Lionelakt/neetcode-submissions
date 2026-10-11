class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_valid(i,j):
            return ( 
            0 <= i < rows 
            and 0 <= j < cols
            and grid[i][j] == 1
            and (not (i,j) in visited))
        
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        
        self.max_area = 0
        L = [self.max_area]  
        def dfs(node):
            
            visited.add(node)
            self.max_area += 1
            
            for di, dj in dirs:
                ni, nj = node[0] + di, node[1] +dj
                if is_valid(ni, nj):
                    dfs((ni,nj))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not (i,j) in visited:
                    
                    dfs((i,j))
                    L.append(self.max_area)
                    self.max_area = 0
        return max(L)

                    


        
        



        
        



