class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        self.heap_size = len(nums)
        for num in nums:
            heapq.heappush(self.min_heap, num)
        for i in range(len(nums)-k-1):
            heapq.heappop(self.min_heap)
            self.heap_size -= 1
        return

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        self.heap_size += 1
        while self.heap_size > self.k:
            remove = heapq.heappop(self.min_heap)
            self.heap_size -= 1
        selected = heapq.heappop(self.min_heap)
        heapq.heappush(self.min_heap, selected)
        print(self.min_heap)
        
        return selected
