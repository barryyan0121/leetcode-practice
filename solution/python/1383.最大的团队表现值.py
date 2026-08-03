# @lc app=leetcode.cn id=1383 lang=python3
import heapq
from typing import List


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        speed_sum = result = 0
        for current_efficiency, current_speed in engineers:
            heapq.heappush(heap, current_speed)
            speed_sum += current_speed
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            result = max(result, speed_sum * current_efficiency)
        return result % (10**9 + 7)


if __name__ == "__main__":
    test_cases = [
        (
            Solution().maxPerformance,
            (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2),
            60,
        ),
        (
            Solution().maxPerformance,
            (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3),
            68,
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1383 题 "最大的团队表现值" 所有测试用例通过')
