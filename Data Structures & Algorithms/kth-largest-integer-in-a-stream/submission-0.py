import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        k_smallest = heapq.nlargest(self.k, self.nums)
        return k_smallest[-1]

