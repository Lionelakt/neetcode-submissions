class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, mid, r = 0, (len(nums) - 1)//2, len(nums)-1

        if nums[l] <= nums[r]:
            return nums[l]
        
        while nums[mid]<= nums[mid+1]:
            if nums[l] <= nums[mid]:
                l = mid
                mid = (l + r)//2
            elif nums[l] >= nums[mid]:
                r = mid
                mid = (l + r)//2
        return nums[mid+1]

            
        