#
# @lc app=leetcode.cn id=158 lang=python3
# @lcpr version=30203
#
# [158] 用 Read4 读取 N 个字符 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# The judge provides read4.
def read4(buf4: List[str]) -> int:  # pragma: no cover
    raise NotImplementedError


# @lc code=start
class Solution:
    def __init__(self):
        self.buf4 = [""] * 4
        self.idx4 = 0
        self.size4 = 0

    def read(self, buf: List[str], n: int) -> int:
        copied = 0
        while copied < n:
            if self.idx4 == self.size4:
                self.size4 = read4(self.buf4)
                self.idx4 = 0
                if self.size4 == 0:
                    break

            while copied < n and self.idx4 < self.size4:
                buf[copied] = self.buf4[self.idx4]
                copied += 1
                self.idx4 += 1

        return copied


# @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    def run_case(data: str, calls: List[int]) -> List[str]:
        global read4
        ptr = 0

        def mock_read4(buf4: List[str]) -> int:
            nonlocal ptr
            count = 0
            while count < 4 and ptr < len(data):
                buf4[count] = data[ptr]
                ptr += 1
                count += 1
            return count

        read4 = mock_read4
        solution = Solution()
        outputs = []
        for n in calls:
            buf = [""] * n
            count = solution.read(buf, n)
            outputs.append("".join(buf[:count]))
        return outputs

    test_cases = [
        (lambda: run_case("abcde", [3, 4]), ["abc", "de"]),
        (lambda: run_case("abcdef", [1, 2, 3, 4]), ["a", "bc", "def", ""]),
        (lambda: run_case("", [1]), [""]),
    ]

    all_passed = True
    for idx, (func, expected) in enumerate(test_cases):
        try:
            result = func()
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {expected}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {expected}, 期望 = {expected}, 实际 = {result}"
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
# "abcde"\n3\n4\n
# @lcpr case=end
