import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            comp = stones[-1] - stones[-2]
            if comp == 0:
                stones.pop()
                stones.pop()
            elif comp<0:
                stones[-2] = -comp
                del stones[-1]
            else:
                stones[-1] = comp
                del stones[-2]
        return stones[0] if len(stones) == 1 else comp

