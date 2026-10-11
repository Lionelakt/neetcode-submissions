class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[1], nums[0])
        cur = prev1
        for i in range(2, len(nums)):
            cur = max(prev2+nums[i], prev1)
            prev2 = prev1
            prev1 = cur
        return cur

"""
        dp = [0]*len(nums)
        if len(nums)==1:
            return nums[0]
        if len(nums)>1:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], 
                dp[i-1])
        return dp[-1]
"""