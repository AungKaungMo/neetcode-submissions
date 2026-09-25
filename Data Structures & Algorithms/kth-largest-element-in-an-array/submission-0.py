class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-v for v in nums]
        heapq.heapify(max_heap)
        count = 1

        while k > count:
            heapq.heappop(max_heap)
            count += 1
        
        return -max_heap[0] if max_heap else 0
