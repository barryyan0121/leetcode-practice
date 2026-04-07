#
# @lc app=leetcode.cn id=281 lang=python3
# @lcpr version=30203
#
# [281] 锯齿迭代器
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


# @lc code=start
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque()
        if v1:
            self.queue.append(deque(v1))
        if v2:
            self.queue.append(deque(v2))

    def next(self) -> int:
        cur = self.queue.popleft()
        val = cur.popleft()
        if cur:
            self.queue.append(cur)
        return val

    def hasNext(self) -> bool:
        return bool(self.queue)
        # @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    test_cases = [
        (
            [("init", [[1, 2], [3, 4, 5, 6]]), ("hasNext", []), ("next", []), ("next", []), ("next", []), ("next", []), ("next", []), ("next", []), ("hasNext", [])],
            [None, True, 1, 3, 2, 4, 5, 6, False],
        ),
        (
            [("init", [[], [1]]), ("hasNext", []), ("next", []), ("hasNext", [])],
            [None, True, 1, False],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            obj = None
            for op, args in ops:
                if op == "init":
                    obj = ZigzagIterator(*args)
                    result.append(None)
                elif op == "next":
                    result.append(obj.next())
                else:
                    result.append(obj.hasNext())
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {ops}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {ops}, 期望 = {expected}, 实际 = {result}"
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
# [1,2]\n[3,4,5,6]\n
# @lcpr case=end

#
