from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dirs_4 = [(0,-1), (0,1), (1,0), (-1,0)]
        visited = set()
        rotten_oranges = deque([])
        fresh_count = 0
        time_0 = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_oranges.append((i,j, time_0))
                elif grid[i][j] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        def is_valid(node: Tuple) -> bool:
            i, j = node[0], node[1]
            return 0 <= i < rows\
            and    0 <= j < cols\
            and    grid[i][j] == 1\
            and    (i,j) not in visited
        ans = 0
        while rotten_oranges:
            (i,j, time) = rotten_oranges.pop()
            ans = max(ans,time)
            if (i,j) not in visited:
                visited.add((i,j))
                for di, dj in dirs_4:
                    ni, nj = i+di, j+dj
                    if is_valid((ni,nj)):
                        grid[ni][nj] = 2
                        rotten_oranges.appendleft((ni,nj, time+1))
                        fresh_count -= 1

        return -1 if fresh_count != 0 else ans
""" mieux vu! BFS EN COUCHES
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # init: multi-source
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        while q and fresh > 0:
            # on traite une "couche" = une minute
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
            minutes += 1

        return minutes if fresh == 0 else -1
"""
        


        

    
        