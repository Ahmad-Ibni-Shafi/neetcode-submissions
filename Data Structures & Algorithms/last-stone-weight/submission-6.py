import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones)==1:
        #     return stones[0]
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a==b:
                continue
            val = a-b
            heapq.heappush(stones, val)
        
        return abs(stones[0]) if stones else 0

        