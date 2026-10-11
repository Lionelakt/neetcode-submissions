import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        result = []
        for elt in nums:
            if elt not in dicti:
                dicti[elt] = 0
            dicti[elt] += 1
        for elt, occurrence in dicti.items():
            heapq.heappush(result, (-occurrence, elt))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(result)[1])
        return res
        

        