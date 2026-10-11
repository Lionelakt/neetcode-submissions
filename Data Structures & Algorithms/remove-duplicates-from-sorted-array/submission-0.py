class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            i, j = 0, 0
            while j < len(nums)-1:
                if nums[j] != nums[j+1]:
                    i += 1
                    nums[i] = nums[j+1]
                j+=1
            return i+1


