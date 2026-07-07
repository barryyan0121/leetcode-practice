#
# @lc app=leetcode.cn id=636 lang=python3
# @lcpr version=30203
#
# [636] 函数的独占时间
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev = 0
        for log in logs:
            fid_s, typ, time_s = log.split(":")
            fid, time = int(fid_s), int(time_s)
            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev
                stack.append(fid)
                prev = time
            else:
                ans[stack.pop()] += time - prev + 1
                prev = time + 1
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.exclusiveTime,
            (2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]),
            [3, 4],
        ),
        (solution.exclusiveTime, (1, ["0:start:0", "0:end:0"]), [1]),
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
