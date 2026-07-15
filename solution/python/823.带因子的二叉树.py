#
# @lc app=leetcode.cn id=823 lang=python3
#
# [823] 带因子的二叉树
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        trees = {}
        for index, value in enumerate(sorted(arr)):
            trees[value] = 1
            for factor in list(trees)[:index]:
                if value % factor == 0 and value // factor in trees:
                    trees[value] = (
                        trees[value] + trees[factor] * trees[value // factor]
                    ) % 1_000_000_007
        return sum(trees.values()) % 1_000_000_007


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numFactoredBinaryTrees, ([2, 4],), 3),
        (solution.numFactoredBinaryTrees, ([2, 4, 5, 10],), 7),
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
