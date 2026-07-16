#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(log):
            identifier, content = log.split(" ", 1)
            return (1,) if content[0].isdigit() else (0, content, identifier)

        return sorted(logs, key=key)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.reorderLogFiles,
            (
                [
                    "dig1 8 1 5 1",
                    "let1 art can",
                    "dig2 3 6",
                    "let2 own kit dig",
                    "let3 art zero",
                ],
            ),
            [
                "let1 art can",
                "let3 art zero",
                "let2 own kit dig",
                "dig1 8 1 5 1",
                "dig2 3 6",
            ],
        ),
        (
            solution.reorderLogFiles,
            (["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],),
            ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
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
