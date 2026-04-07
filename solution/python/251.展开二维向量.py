#
# @lc app=leetcode.cn id=251 lang=python3
# @lcpr version=30203
#
# [251] 展开二维向量
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = 0

    def _advance(self) -> None:
        while self.row < len(self.vec) and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        self._advance()
        value = self.vec[self.row][self.col]
        self.col += 1
        return value

    def hasNext(self) -> bool:
        self._advance()
        return self.row < len(self.vec)


# @lc code=end


if __name__ == "__main__":
    def run_operations(ops: List[str], values: List[List[Any]]) -> List[Optional[Union[int, bool]]]:
        iterator = None
        result = []

        for op, value in zip(ops, values):
            if op == "Vector2D":
                iterator = Vector2D(value)
                result.append(None)
            elif op == "next":
                result.append(iterator.next())
            elif op == "hasNext":
                result.append(iterator.hasNext())
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"],
                [[[1, 2], [3], [4]], [], [], [], [], [], [], []],
            ),
            [None, 1, 2, 3, True, True, 4, False],
        ),
        (
            run_operations,
            (
                ["Vector2D", "hasNext", "next", "hasNext"],
                [[[], [5]], [], [], []],
            ),
            [None, True, 5, False],
        ),
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
# ["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]\n[[[1,2],[3],[4]],[],[],[],[],[],[],[]]\n
# @lcpr case=end
