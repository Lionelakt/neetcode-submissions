class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        n = len(coins)
        def dp(i, s):
            if (i,s) in memo:
                return memo[(i,s)]
            if i ==  0 and s == 0:
                return 1
            if i == 0 and s>0:
                return 0

            if s-coins[i-1] >= 0: 
                memo[(i,s)] = dp(i-1, s) + dp(i, s-coins[i-1])
            else:
                memo[(i,s)] = dp(i-1, s)
            return memo[(i,s)]
        return dp(n, amount)
