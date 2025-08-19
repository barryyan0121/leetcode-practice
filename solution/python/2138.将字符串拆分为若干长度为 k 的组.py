#
# @lc app=leetcode.cn id=2138 lang=python3
# @lcpr version=30202
#
# [2138] 将字符串拆分为若干长度为 k 的组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        for i in range(0, n, k):
            part = s[i : i + k]
            if len(part) < k:
                part += fill * (k - len(part))
            res.append(part)
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.divideString, ("abcdefghi", 3, "x"), ["abc", "def", "ghi"]),
        (solution.divideString, ("abcdefghij", 3, "x"), ["abc", "def", "ghi", "jxx"]),
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
# "abcdefghi"\n3\n"x"\n
# @lcpr case=end

# @lcpr case=start
# "abcdefghij"\n3\n"x"\n
# @lcpr case=end

#
