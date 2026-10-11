class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        return dp(n)

"""        if n<= 2:
            return n

        dp = [0]*n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]"""