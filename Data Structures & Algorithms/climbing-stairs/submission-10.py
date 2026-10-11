class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        """if n > 2:
            dp = [0]*(n)
            dp[1] = 1
            dp[2] = 2
            for i in range(3, n):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]"""

        prev1 = 2
        prev2 = 1
        for i in range(n-2):
            prev = prev1 + prev2
            prev2 = prev1
            prev1 = prev

        return prev1

