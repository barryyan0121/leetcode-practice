#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30202
#
# [146] LRU 缓存
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import OrderedDict
from common.node import *


# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        # @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    test_cases = [
        (
            [
                ("init", [2]),
                ("put", [1, 1]),
                ("put", [2, 2]),
                ("get", [1]),
                ("put", [3, 3]),
                ("get", [2]),
                ("put", [4, 4]),
                ("get", [1]),
                ("get", [3]),
                ("get", [4]),
            ],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ),
        (
            [
                ("init", [1]),
                ("put", [2, 1]),
                ("get", [2]),
                ("put", [3, 2]),
                ("get", [2]),
                ("get", [3]),
            ],
            [None, None, 1, None, -1, 2],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            cache = None
            for op, args in ops:
                if op == "init":
                    cache = LRUCache(*args)
                    result.append(None)
                elif op == "put":
                    result.append(cache.put(*args))
                else:
                    result.append(cache.get(*args))
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
# 2\n
# ["put","put","get","put","get","get"]\n[1,1]\n[2,2]\n[1]\n[3,3]\n[2]\n[3]\n
# @lcpr case=end

#
