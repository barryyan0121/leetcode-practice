#
# @lc app=leetcode.cn id=833 lang=python3
#
# [833] 字符串中的查找与替换
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def findReplaceString(
        self,
        s: str,
        indices: List[int],
        sources: List[str],
        targets: List[str],
    ) -> str:
        replacements = {}
        for index, source, target in zip(indices, sources, targets):
            replacements.setdefault(index, []).append((source, target))
        answer = []
        index = 0
        while index < len(s):
            replacement = next(
                (
                    replacement
                    for replacement in replacements.get(index, [])
                    if s.startswith(replacement[0], index)
                ),
                None,
            )
            if replacement:
                source, target = replacement
                answer.append(target)
                index += len(source)
            else:
                answer.append(s[index])
                index += 1
        return "".join(answer)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findReplaceString,
            ("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]),
            "eeebffff",
        ),
        (
            solution.findReplaceString,
            ("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]),
            "eeecd",
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
