class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        for i in range(n):
            maxi = max((dp[j] for j in range(i)
                if nums[j] < nums[i]), default = 0
                )
            dp[i] = 1 + maxi
        return max(dp)

