class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}
        def dp(i):
            if i in memo:
                return memo[i]
            mini = float('inf')

            for c in coins:
                prev = i - c
                if prev>=0:
                    dprev = dp(prev)
                    memo[prev] = dprev
                    if dprev != -1:
                        mini = min(mini, dprev+1)

            memo[i] = mini if mini<float('inf') else -1
            return memo[i]
        
        return dp(amount)