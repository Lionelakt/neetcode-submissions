class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        n = len(nums)
        if (sum(nums)+target) < 0 or  (sum(nums)+target)%2 != 0:
            return 0
        p = (sum(nums)+target)//2

        def dp(i, s):
            if s == 0 and i == 0:
                return 1
            if i == 0 and s > 0:
                return 0
            if (i,s) in memo:
                return memo[(i,s)]

            if s-nums[i-1]>=0:
                memo[(i,s)] = dp(i-1, s) + dp(i-1, s-nums[i-1])
            else:
                memo[(i,s)] = dp(i-1, s)
                
            return memo[(i,s)]
        return dp(n, p)