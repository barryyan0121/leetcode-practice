#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [len(s)] * len(s)
        previous = -len(s)
        for index, character in enumerate(s):
            if character == c:
                previous = index
            answer[index] = index - previous
        previous = 2 * len(s)
        for index in range(len(s) - 1, -1, -1):
            if s[index] == c:
                previous = index
            answer[index] = min(answer[index], previous - index)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.shortestToChar,
            ("loveleetcode", "e"),
            [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0],
        ),
        (solution.shortestToChar, ("aaab", "b"), [3, 2, 1, 0]),
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
