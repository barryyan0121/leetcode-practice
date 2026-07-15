#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

import os
import sys


# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        answer = 0
        previous = None
        index = 0
        while n:
            if n & 1:
                if previous is not None:
                    answer = max(answer, index - previous)
                previous = index
            n >>= 1
            index += 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.binaryGap, (22,), 2),
        (solution.binaryGap, (8,), 0),
        (solution.binaryGap, (5,), 2),
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
