"""2208. 将数组和减半的最少操作次数"""

import heapq


class Solution:
    def halveArray(self, nums: list[int]) -> int:
        heap = [-2 * value for value in nums]
        heapq.heapify(heap)
        target = sum(nums)
        reduced = 0
        steps = 0
        while reduced * 2 < target:
            value = -heapq.heappop(heap)
            reduced += value
            half = value // 2
            reduced -= half
            heapq.heappush(heap, -half)
            steps += 1
        return steps
