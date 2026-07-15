#
# @lc app=leetcode.cn id=745 lang=python3
#
# [745] 前缀和后缀搜索
#

import os
import sys
from typing import *


# @lc code=start
class WordFilter:
    def __init__(self, words: List[str]):
        self.indices = {}
        for index, word in enumerate(words):
            for prefix_length in range(len(word) + 1):
                for suffix_length in range(len(word) + 1):
                    self.indices[
                        word[:prefix_length] + "#" + word[len(word) - suffix_length :]
                    ] = index

    def f(self, pref: str, suff: str) -> int:
        return self.indices.get(pref + "#" + suff, -1)


# @lc code=end


if __name__ == "__main__":
    obj = WordFilter(["apple"])
    test_cases = [
        (obj.f, ("a", "e"), 0),
        (obj.f, ("b", ""), -1),
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
