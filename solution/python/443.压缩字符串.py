#
# @lc app=leetcode.cn id=443 lang=python3
# @lcpr version=30203
#
# [443] 压缩字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            start = read
            while read < len(chars) and chars[read] == char:
                read += 1
            chars[write] = char
            write += 1
            count = read - start
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    chars2 = ["a"]
    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

    test_cases = [
        (solution.compress, (chars1,), (6, ["a", "2", "b", "2", "c", "3"])),
        (solution.compress, (chars2,), (1, ["a"])),
        (solution.compress, (chars3,), (4, ["a", "b", "1", "2"])),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            expected_len, expected_chars = expected
            assert result == expected_len
            assert args[0][:result] == expected_chars
            print(
                f"测试用例 {idx + 1} 通过: n = {args}, result = {(result, args[0][:result])}"
            )
        except AssertionError:
            all_passed = False
            actual = (result, args[0][:result]) if "result" in locals() else None
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {actual}"
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
# ["a","a","b","b","c","c","c"]\n
# @lcpr case=end
