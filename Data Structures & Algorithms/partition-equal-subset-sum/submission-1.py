class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0:
            return False
        half = total//2

        memo = {}

        def dp(i,w):
            if (i,w) in memo:
                return memo[(i,w)]
            if i == 0:
                return False
            if w == 0:
                return True
            
            skip = dp(i-1, w)
            include = dp(i-1, w-nums[i-1]) and w-nums[i-1]>=0

            memo[(i,w)] = skip or include
            return memo[(i,w)]
        return dp(n ,half)

            
            
