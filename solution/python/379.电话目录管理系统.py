#
# @lc app=leetcode.cn id=379 lang=python3
# @lcpr version=30203
#
# [379] 电话目录管理系统
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.available = set(range(maxNumbers))
        self.next = 0

    def get(self) -> int:
        if self.next < self.maxNumbers:
            while self.next < self.maxNumbers and self.next not in self.available:
                self.next += 1
            if self.next < self.maxNumbers:
                num = self.next
                self.available.remove(num)
                self.next += 1
                return num
        if not self.available:
            return -1
        num = min(self.available)
        self.available.remove(num)
        return num

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        if 0 <= number < self.maxNumbers:
            self.available.add(number)
            if number < self.next:
                self.next = number
        # @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    test_cases = [
        (
            [
                ("init", [3]),
                ("get", []),
                ("get", []),
                ("check", [2]),
                ("get", []),
                ("check", [2]),
                ("release", [2]),
                ("check", [2]),
            ],
            [None, 0, 1, True, 2, False, None, True],
        ),
        (
            [
                ("init", [1]),
                ("check", [0]),
                ("get", []),
                ("check", [0]),
                ("get", []),
            ],
            [None, True, 0, False, -1],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            obj = None
            for op, args in ops:
                if op == "init":
                    obj = PhoneDirectory(*args)
                    result.append(None)
                elif op == "get":
                    result.append(obj.get())
                elif op == "check":
                    result.append(obj.check(*args))
                else:
                    result.append(obj.release(*args))
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
# 3\n
# ["PhoneDirectory","get","get","check","get","check","release","check"]\n[[],[],[],[2],[],[2],[2],[2]]\n
# @lcpr case=end

#
