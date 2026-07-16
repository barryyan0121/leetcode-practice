#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        answer = []
        for character in s:
            if character == "I":
                answer.append(low)
                low += 1
            else:
                answer.append(high)
                high -= 1
        return answer + [low]


# @lc code=end


def valid(pattern, result):
    return sorted(result) == list(range(len(pattern) + 1)) and all(
        (first < second) == (direction == "I")
        for first, second, direction in zip(result, result[1:], pattern)
    )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.diStringMatch, ("IDID",), valid),
        (solution.diStringMatch, ("III",), valid),
        (solution.diStringMatch, ("DDI",), valid),
    ]
    all_passed = True
    for idx, (func, args, checker) in enumerate(test_cases):
        result = func(*args)
        expected = checker(args[0], result)
        try:
            assert expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 实际 = {result}")
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
