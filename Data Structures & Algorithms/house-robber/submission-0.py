import heapq
class Solution:
    def rob(self, nums: List[int]) -> int:
        """dp = [0]*(len(nums))

        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]"""

        #ou
        prev1 = 0
        prev2 = 0

        for x in nums:
            prev =  max(prev1, prev2 + x)
            prev2 = prev1
            prev1 = prev
        return prev1
