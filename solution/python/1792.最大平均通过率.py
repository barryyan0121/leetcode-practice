#
# @lc app=leetcode.cn id=1792 lang=python3
# @lcpr version=30202
#
# [1792] 最大平均通过率
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import List
from common.node import *
from heapq import heapify, heapreplace


# @lc code=start
class Entry:
    __slots__ = "p", "t"

    def __init__(self, p: int, t: int):
        self.p = p
        self.t = t

    def __lt__(self, b: "Entry") -> bool:
        return (self.t - self.p) * b.t * (b.t + 1) > (b.t - b.p) * self.t * (self.t + 1)


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)
        for _ in range(extraStudents):
            heapreplace(h, Entry(h[0].p + 1, h[0].t + 1))
        return sum(e.p / e.t for e in h) / len(h)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxAverageRatio, ([[1, 2], [3, 5], [2, 2]], 2), 0.78333),
        (solution.maxAverageRatio, ([[2, 4], [3, 9], [4, 5], [2, 10]], 4), 0.53485),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert round(result,5) == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# [[1,2],[3,5],[2,2]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[2,4],[3,9],[4,5],[2,10]]\n4\n
# @lcpr case=end

#
