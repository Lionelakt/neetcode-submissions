class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0]==target else -1
        l, mid, r = 0, (len(nums)-1)//2, len(nums)-1
        if nums[l] <= nums[r]:
            mid = None
        else:
            while nums[mid]<nums[mid+1]:
                if nums[l] <= nums[mid]:
                    l = mid
                    mid = (l + r)//2
                else:
                    r = mid
                    mid = (l + r)//2
        deflection = mid
        if deflection != None:
            for (lo, hi) in [(0, deflection), (deflection+1, len(nums)-1)]:
                while lo<= hi:
                    mid = (lo + hi)//2
                    if target == nums[mid]:
                        return mid
                    if target < nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
        else:
            lo, hi = 0, len(nums)-1

            while lo<= hi:
                mid = (lo + hi)//2
                if target == nums[mid]:
                    return mid
                if target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

        return -1

                

        