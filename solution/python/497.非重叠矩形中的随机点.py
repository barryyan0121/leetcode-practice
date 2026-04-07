#
# @lc app=leetcode.cn id=497 lang=python3
# @lcpr version=30203
#
# [497] 非重叠矩形中的随机点
#

import sys
import os
import random
from bisect import bisect_right

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0
        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)

    def pick(self) -> List[int]:
        target = random.randint(1, self.prefix[-1])
        idx = bisect_right(self.prefix, target - 1)
        x1, y1, x2, y2 = self.rects[idx]
        width = x2 - x1 + 1
        offset = target - (self.prefix[idx - 1] if idx else 0) - 1
        return [x1 + offset // (y2 - y1 + 1), y1 + offset % (y2 - y1 + 1)]


# @lc code=end


if __name__ == "__main__":
    solution = Solution([[1, 1, 2, 2], [3, 3, 3, 3]])

    def run_case(rects: List[List[int]], picks: int = 20) -> bool:
        obj = Solution(rects)
        random.seed(0)
        for _ in range(picks):
            x, y = obj.pick()
            assert any(x1 <= x <= x2 and y1 <= y <= y2 for x1, y1, x2, y2 in rects)
        return True

    test_cases = [
        (run_case, ([[1, 1, 2, 2], [3, 3, 3, 3]],), True),
        (run_case, ([[0, 0, 0, 0]],), True),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
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
# [[1,1,2,2],[3,3,3,3]]\n
# @lcpr case=end

#
