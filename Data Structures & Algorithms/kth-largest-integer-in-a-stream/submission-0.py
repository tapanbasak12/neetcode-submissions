class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums=nums
        self.heap=[]

        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            else:
                heapq.heappushpop(self.heap, i)
            

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        
        return self.heap[0]
        

        
        

