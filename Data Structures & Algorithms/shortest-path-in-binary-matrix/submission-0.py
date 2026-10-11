from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        dirs_8 = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0),  (1,1)]

        q = deque([(0, 0, 1)])  # (i, j, distance). distance=1 car on compte la case de départ
        visited = {(0, 0)}

        while q:
            i, j, d = q.popleft()

            if (i, j) == (n-1, n-1):
                return d

            for di, dj in dirs_8:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    q.append((ni, nj, d + 1))

        return -1
