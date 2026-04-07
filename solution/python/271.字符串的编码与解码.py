#
# @lc app=leetcode.cn id=271 lang=python3
# @lcpr version=30203
#
# [271] 字符串的编码与解码
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Codec:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            result.append(s[start : start + length])
            i = start + length
        return result


# @lc code=end


if __name__ == "__main__":
    codec = Codec()
    # 测试用例 (func, args, result)
    test_cases = [
        (codec.decode, (codec.encode(["lint", "code", "love", "you"]),), ["lint", "code", "love", "you"]),
        (codec.decode, (codec.encode(["", "a", "b"]),), ["", "a", "b"]),
        (codec.decode, (codec.encode(["#:", "12#3"]),), ["#:", "12#3"]),
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
# ["lint","code","love","you"]\n
# @lcpr case=end
