#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

import os
import sys
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        left = 0
        answer = 0
        for right, fruit in enumerate(fruits):
            counts[fruit] += 1
            while len(counts) > 2:
                removed = fruits[left]
                counts[removed] -= 1
                if not counts[removed]:
                    del counts[removed]
                left += 1
            answer = max(answer, right - left + 1)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.totalFruit, ([1, 2, 1],), 3),
        (solution.totalFruit, ([0, 1, 2, 2],), 3),
        (solution.totalFruit, ([1, 2, 3, 2, 2],), 4),
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
