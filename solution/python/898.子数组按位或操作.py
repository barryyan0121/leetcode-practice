#
# @lc app=leetcode.cn id=898 lang=python3
#
# [898] 子数组按位或操作
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        answer = set()
        ending = set()
        for value in arr:
            ending = {value | previous for previous in ending} | {value}
            answer |= ending
        return len(answer)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.subarrayBitwiseORs, ([0],), 1),
        (solution.subarrayBitwiseORs, ([1, 1, 2],), 3),
        (solution.subarrayBitwiseORs, ([1, 2, 4],), 6),
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
