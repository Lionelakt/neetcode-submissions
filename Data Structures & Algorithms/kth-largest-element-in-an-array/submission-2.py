import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n_largest = heapq.nlargest(k, nums)
        return n_largest[-1]