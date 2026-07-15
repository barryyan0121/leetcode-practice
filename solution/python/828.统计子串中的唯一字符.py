#
# @lc app=leetcode.cn id=828 lang=python3
#
# [828] 统计子串中的唯一字符
#

import os
import sys


# @lc code=start
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        previous = [-1] * 26
        last = [-1] * 26
        answer = 0
        for index, character in enumerate(s):
            letter = ord(character) - 65
            answer += (index - last[letter]) * (last[letter] - previous[letter])
            previous[letter], last[letter] = last[letter], index
        for letter in range(26):
            answer += (len(s) - last[letter]) * (last[letter] - previous[letter])
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.uniqueLetterString, ("ABC",), 10),
        (solution.uniqueLetterString, ("ABA",), 8),
        (solution.uniqueLetterString, ("LEETCODE",), 92),
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
