#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

import os
import sys


# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        values = [1, 1, 2]
        for index in range(3, n + 1):
            values.append((2 * values[index - 1] + values[index - 3]) % 1_000_000_007)
        return values[n]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numTilings, (1,), 1),
        (solution.numTilings, (3,), 5),
        (solution.numTilings, (5,), 24),
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
