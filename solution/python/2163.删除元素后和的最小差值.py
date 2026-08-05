"""2163. 删除元素后和的最小差值"""

import heapq


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        left = [0] * (2 * n + 1)
        heap = []
        total = 0
        for i, value in enumerate(nums[: 2 * n]):
            heapq.heappush(heap, -value)
            total += value
            if len(heap) > n:
                total += heapq.heappop(heap)
            if i + 1 >= n:
                left[i + 1] = total
        right = [0] * (2 * n + 1)
        heap = []
        total = 0
        for i in range(3 * n - 1, n - 1, -1):
            value = nums[i]
            heapq.heappush(heap, value)
            total += value
            if len(heap) > n:
                total -= heapq.heappop(heap)
            if i <= 2 * n:
                right[i] = total
        return min(left[i] - right[i] for i in range(n, 2 * n + 1))


if __name__ == "__main__":
    test_cases = [(([3, 1, 2],), -1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumDifference(*args) == expected
