class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def helper(nums_):
            if len(nums_) <= 2:
                return max(nums_)
            prev2, prev1 = nums_[0], max(nums_[0], nums_[1])
            for i in range(2, len(nums_)):
                cur = max(prev2 + nums_[i], prev1)
                prev2 = prev1
                prev1 = cur
            return cur 

        return max(helper(nums[:-1]), helper(nums[1:]))


        """
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
        return max(rob_dp(nums1), rob_dp(nums2))"""