class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        dp  = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

"""
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        memo = {}
        memo[1], memo[2] = nums[0], max(nums[0], nums[1])
        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i-1), dp(i-2) + nums[i-1])
            return memo[i]
        return dp(len(nums))
"""