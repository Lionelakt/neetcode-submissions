class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        my_cost = cost+[0]
        n = len(my_cost)
        dp = [float('inf')]*(len(my_cost))
        dp[0],  dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + my_cost[i]
        return dp[-1]