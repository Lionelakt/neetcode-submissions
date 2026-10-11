from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        dirs_8 = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0),(1,1)]
        start = (0,0)
        chemin = []

        def is_valid(i,j):
            return 0 <= i < rows and 0<= j < cols and grid[i][j] == 0 and (i,j) not in visited
        
        if  grid[0][0] == 1 or  grid[rows-1][cols-1] == 1:
            return -1
        queue = deque([(0,0,1)])
        while queue:
            (i,j,d) = queue.popleft()

            if (i,j) == (rows-1,cols-1):
                return d
            if (i,j) not in visited:
                chemin.append((i,j))
                visited.add((i,j))
                for di, dj in dirs_8:
                    if is_valid(i+di, j+dj):
                        queue.append((i+di, j+dj,d+1))
        return -1

        
        
            
                        
            






            

