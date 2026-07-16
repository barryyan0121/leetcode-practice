#
# @lc app=leetcode.cn id=906 lang=python3
#
# [906] 超级回文数
#

import os
import sys


# @lc code=start
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        lower, upper = int(left), int(right)
        answer = 0
        for seed in range(1, 100_000):
            text = str(seed)
            for root in (int(text + text[-2::-1]), int(text + text[::-1])):
                square = root * root
                if lower <= square <= upper and str(square) == str(square)[::-1]:
                    answer += 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.superpalindromesInRange, ("4", "1000"), 4),
        (solution.superpalindromesInRange, ("1", "2"), 1),
        (
            solution.superpalindromesInRange,
            ("40000000000000000", "50000000000000000"),
            2,
        ),
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
