#
# @lc app=leetcode.cn id=359 lang=python3
# @lcpr version=30203
#
# [359] 日志速率限制器
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Logger:
    def __init__(self):
        self.last = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last or timestamp - self.last[message] >= 10:
            self.last[message] = timestamp
            return True
        return False


# @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    def run_operations(ops: List[str], values: List[List[Any]]) -> List[Optional[bool]]:
        logger = None
        result = []
        for op, value in zip(ops, values):
            if op == "Logger":
                logger = Logger()
                result.append(None)
            elif op == "shouldPrintMessage":
                result.append(logger.shouldPrintMessage(value[0], value[1]))
        return result

    test_cases = [
        (
            run_operations,
            (
                [
                    "Logger",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                    "shouldPrintMessage",
                ],
                [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"]],
            ),
            [None, True, True, False, False, False],
        ),
        (
            run_operations,
            (
                ["Logger", "shouldPrintMessage", "shouldPrintMessage"],
                [[], [1, "a"], [11, "a"]],
            ),
            [None, True, True],
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
# ["Logger","shouldPrintMessage","shouldPrintMessage"]\n[[],[1,"foo"],[2,"bar"]]\n
# @lcpr case=end
