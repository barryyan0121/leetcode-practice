#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#

import os
import sys


# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(-1, "L")]
        symbols.extend((i, value) for i, value in enumerate(dominoes) if value != ".")
        symbols.append((len(dominoes), "R"))
        answer = list(dominoes)
        for (left, left_value), (right, right_value) in zip(symbols, symbols[1:]):
            if left_value == right_value:
                answer[left + 1 : right] = left_value * (right - left - 1)
            elif left_value == "R" and right_value == "L":
                for offset in range((right - left - 1) // 2):
                    answer[left + offset + 1] = "R"
                    answer[right - offset - 1] = "L"
        return "".join(answer)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.pushDominoes, ("RR.L",), "RR.L"),
        (solution.pushDominoes, (".L.R...LR..L..",), "LL.RR.LLRRLL.."),
        (solution.pushDominoes, ("R...L",), "RR.LL"),
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
