import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []
        heapq.heapify(distances)
        for point in points:
            heapq.heappush(distances, (point[0]**2 + point[1]**2, point ))
        distances = heapq.nsmallest(k, distances)
        return [elt[1] for elt in distances]