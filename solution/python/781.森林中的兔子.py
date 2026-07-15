#
# @lc app=leetcode.cn id=781 lang=python3
#
# [781] 森林中的兔子
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum(
            (count + answer) // (answer + 1) * (answer + 1)
            for answer, count in Counter(answers).items()
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numRabbits, ([1, 1, 2],), 5),
        (solution.numRabbits, ([10, 10, 10],), 11),
        (solution.numRabbits, ([],), 0),
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
