import heapq

class KthLargest:
    # Awesome solution implemented with min_heap -> beats 99.7% time and 93% space
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k :
            heapq.heappop(self.min_heap)

        return self.min_heap[0]

    def heappop(self, heap:List[int]) -> int:
        pass

    def heappush(self, heap:List[int], val: int):
        pass
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)