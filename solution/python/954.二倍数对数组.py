#
# @lc app=leetcode.cn id=954 lang=python3
#
# [954] 二倍数对数组
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        if counts[0] % 2:
            return False
        for number in sorted(counts, key=abs):
            if counts[2 * number] < counts[number]:
                return False
            counts[2 * number] -= counts[number]
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.canReorderDoubled, ([3, 1, 3, 6],), False),
        (solution.canReorderDoubled, ([2, 1, 2, 6],), False),
        (solution.canReorderDoubled, ([4, -2, 2, -4],), True),
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
