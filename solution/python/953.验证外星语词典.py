#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {character: index for index, character in enumerate(order)}
        for first, second in zip(words, words[1:]):
            for left, right in zip(first, second):
                if left != right:
                    if rank[left] > rank[right]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.isAlienSorted,
            (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
            True,
        ),
        (
            solution.isAlienSorted,
            (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"),
            False,
        ),
        (
            solution.isAlienSorted,
            (["apple", "app"], "abcdefghijklmnopqrstuvwxyz"),
            False,
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
