#
# @lc app=leetcode.cn id=157 lang=python3
# @lcpr version=30203
#
# [157] 用 Read4 读取 N 个字符
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *

READ4_DATA = ""
READ4_INDEX = 0


def read4(buf4: List[str]) -> int:
    global READ4_INDEX
    count = 0
    while count < 4 and READ4_INDEX < len(READ4_DATA):
        buf4[count] = READ4_DATA[READ4_INDEX]
        READ4_INDEX += 1
        count += 1
    return count


# @lc code=start
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
class Solution:
    def read(self, buf: List[str], n: int) -> int:
        total = 0
        buf4 = [""] * 4

        while total < n:
            count = read4(buf4)
            if count == 0:
                break

            for i in range(min(count, n - total)):
                buf[total] = buf4[i]
                total += 1

        return total


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def run_case(content: str, n: int) -> List[Union[int, str]]:
        global READ4_DATA, READ4_INDEX
        READ4_DATA = content
        READ4_INDEX = 0
        buf = [""] * max(1, n)
        read_chars = solution.read(buf, n)
        return [read_chars, "".join(buf[:read_chars])]

    # 测试用例 (func, args, result)
    test_cases = [
        (run_case, ("abc", 4), [3, "abc"]),
        (run_case, ("abcde", 4), [4, "abcd"]),
        (run_case, ("", 1), [0, ""]),
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
# "abc"\n4\n
# @lcpr case=end
