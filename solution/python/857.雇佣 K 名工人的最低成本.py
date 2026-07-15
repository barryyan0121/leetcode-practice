#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#

import os
import sys
from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        workers = sorted((w / q, q) for q, w in zip(quality, wage))
        qualities = []
        total_quality = 0
        answer = float("inf")
        for ratio, worker_quality in workers:
            heappush(qualities, -worker_quality)
            total_quality += worker_quality
            if len(qualities) > k:
                total_quality += heappop(qualities)
            if len(qualities) == k:
                answer = min(answer, ratio * total_quality)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.mincostToHireWorkers, ([10, 20, 5], [70, 50, 30], 2), 105.0),
        (
            solution.mincostToHireWorkers,
            ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3),
            30.666666666666664,
        ),
        (solution.mincostToHireWorkers, ([1], [1], 1), 1.0),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert abs(result - expected) < 1e-5
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
