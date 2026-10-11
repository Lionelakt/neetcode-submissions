class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(lo, hi):
            if lo>hi:
                return -1
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return helper(mid+1, hi)
            else:
                return helper(lo, mid-1)
        return helper(0, len(nums)-1)
            
        
