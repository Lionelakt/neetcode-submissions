class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        n = len(cost)
        memo = {}
        memo[0], memo[1] = 0, 0
        
        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            return memo[i]
        return dp(n)
        """
        if len(cost) <= 2:
            return min(cost)
        my_cost = cost+[0]
        n = len(my_cost)
        dp = [float('inf')]*(len(my_cost))
        dp[0],  dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + my_cost[i]
        return dp[-1]
        """