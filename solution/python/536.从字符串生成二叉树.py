#
# @lc app=leetcode.cn id=536 lang=python3
# @lcpr version=30203
#
# [536] 从字符串生成二叉树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        idx = 0

        def parse() -> TreeNode:
            nonlocal idx
            sign = 1
            if s[idx] == "-":
                sign = -1
                idx += 1

            value = 0
            while idx < len(s) and s[idx].isdigit():
                value = value * 10 + int(s[idx])
                idx += 1

            node = TreeNode(sign * value)
            if idx < len(s) and s[idx] == "(":
                idx += 1
                node.left = parse()
                idx += 1
            if idx < len(s) and s[idx] == "(":
                idx += 1
                node.right = parse()
                idx += 1
            return node

        return parse()


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.str2tree,
            ("4(2(3)(1))(6(5))",),
            "4,2,3,null,null,1,null,null,6,5,null,null,null",
        ),
        (solution.str2tree, ("-4(2)(3)",), "-4,2,null,null,3,null,null"),
        (solution.str2tree, ("1",), "1,null,null"),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            printed = TreeNode.print_tree(result)
            assert printed == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {printed}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {printed}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# 4(2(3)(1))(6(5))\n
# @lcpr case=end
#
