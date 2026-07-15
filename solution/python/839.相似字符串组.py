#
# @lc app=leetcode.cn id=839 lang=python3
#
# [839] 相似字符串组
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = list(range(len(strs)))

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        groups = len(strs)
        for i in range(len(strs)):
            for j in range(i):
                if (
                    find(i) != find(j)
                    and sum(a != b for a, b in zip(strs[i], strs[j])) <= 2
                ):
                    parent[find(i)] = find(j)
                    groups -= 1
        return groups


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numSimilarGroups, (["tars", "rats", "arts", "star"],), 2),
        (solution.numSimilarGroups, (["omv", "ovm"],), 1),
        (solution.numSimilarGroups, (["abc"],), 1),
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
