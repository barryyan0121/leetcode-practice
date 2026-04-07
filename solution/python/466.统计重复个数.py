#
# @lc app=leetcode.cn id=466 lang=python3
# @lcpr version=30203
#
# [466] 统计重复个数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def getMaxRepetitions(
        self, s1: str, n1: int, s2: str, n2: int
    ) -> int:
        if set(s2) - set(s1):
            return 0

        indexr = {}
        s1cnt = s2cnt = index = 0
        while s1cnt < n1:
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        s2cnt += 1
            if index in indexr:
                s1cnt_prev, s2cnt_prev = indexr[index]
                pre_loop_s1 = s1cnt_prev
                pre_loop_s2 = s2cnt_prev
                in_loop_s1 = s1cnt - s1cnt_prev
                in_loop_s2 = s2cnt - s2cnt_prev
                if in_loop_s1 == 0:
                    return s2cnt // n2
                loop = (n1 - pre_loop_s1) // in_loop_s1
                s1cnt = pre_loop_s1 + loop * in_loop_s1
                s2cnt = pre_loop_s2 + loop * in_loop_s2
                break
            else:
                indexr[index] = (s1cnt, s2cnt)

        while s1cnt < n1:
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        s2cnt += 1
        return s2cnt // n2
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.getMaxRepetitions, ["acb", 4, "ab", 2], 2),
        (solution.getMaxRepetitions, ["aaa", 3, "aa", 1], 4),
        (solution.getMaxRepetitions, ["abc", 4, "ab", 2], 2),
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
# "acb"\n4\n"ab"\n2\n
# @lcpr case=end

#
