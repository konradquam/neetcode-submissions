class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []
        for num in nums:
            heapq.heappush_max(self.max_heap, num)
        return

    def add(self, val: int) -> int:
        heapq.heappush_max(self.max_heap, val)
        removed = []
        for i in range(self.k):
            removed.append(heapq.heappop_max(self.max_heap))
        selected = removed[len(removed)-1]
        print(selected)
        for item in removed:
            heapq.heappush_max(self.max_heap, item)
        return selected
