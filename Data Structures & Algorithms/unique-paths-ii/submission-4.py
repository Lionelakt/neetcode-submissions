class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0 or obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1]==1:
            return 0
        
        dp = [0]*n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j-1 >= 0: #si j-1 est valide quoi
                    dp[j] = dp[j] + dp[j-1] 
                    #is the new dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1]

        """La complexité en mémoire est de O(n*m), mais on peut faire du O(n)
        def uniquePathsWithObstacles(self, grid):
            if m == 0 or grid[0][0] == 1 or grid[m-1][n-1] == 0:
                return 0
            dp = [0]*n
            dp[0] = 1

            for i in range(m):
                for j in range(m):
                    if grid[j] == 1:
                        dp[j] = 0
                    elif j-1 >= 0: #si j-1 est valide quoi
                        dp[j] = dp[j] + dp[j-1] 
                        #is the new dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[-1]
            """
        