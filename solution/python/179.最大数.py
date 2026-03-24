#
# @lc app=leetcode.cn id=179 lang=python3
# @lcpr version=30203
#
# [179] 最大数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from functools import cmp_to_key


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        parts = sorted((str(num) for num in nums), key=cmp_to_key(compare))
        result = "".join(parts)
        return "0" if result[0] == "0" else result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.largestNumber, ([10, 2],), "210"),
        (solution.largestNumber, ([3, 30, 34, 5, 9],), "9534330"),
        (solution.largestNumber, ([0, 0],), "0"),
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
# [10,2]\n
# @lcpr case=end
