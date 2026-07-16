#
# @lc app=leetcode.cn id=900 lang=python3
#
# [900] RLE 迭代器
#

import os
import sys
from typing import List


# @lc code=start
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding) and n > self.encoding[self.index]:
            n -= self.encoding[self.index]
            self.index += 2
        if self.index == len(self.encoding):
            return -1
        self.encoding[self.index] -= n
        return self.encoding[self.index + 1]


# @lc code=end


def run_operations(encoding, requests):
    iterator = RLEIterator(encoding)
    return [iterator.next(request) for request in requests]


if __name__ == "__main__":
    test_cases = [
        (run_operations, ([3, 8, 0, 9, 2, 5], [2, 1, 1, 2]), [8, 8, 5, -1]),
        (run_operations, ([1, 7], [1, 1]), [7, -1]),
        (run_operations, ([0, 1, 2, 3], [1, 1, 1]), [3, 3, -1]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
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
