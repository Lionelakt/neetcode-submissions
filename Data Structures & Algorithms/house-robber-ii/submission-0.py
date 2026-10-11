class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<= 2:
            return max(nums)
        nums1 = nums[:-1]
        nums2 = nums[1:]

        def rob_dp(nums_):
            memo = {}
            memo[1], memo[2] = nums_[0], max(nums_[0], nums_[1])
            def dp(i):
                if i in memo:
                    return memo[i]
                memo[i] = max(dp(i-1), dp(i-2)+nums_[i-1])
                return memo[i]
            return dp(len(nums_))
        return max(rob_dp(nums1), rob_dp(nums2))