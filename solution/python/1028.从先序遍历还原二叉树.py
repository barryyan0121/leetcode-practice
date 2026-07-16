#
# @lc app=leetcode.cn id=1028 lang=python3
#
# [1028] 从先序遍历还原二叉树
#

import os
import re
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        stack = []
        for dashes, value in re.findall(r"(-*)(\d+)", traversal):
            depth = len(dashes)
            node = TreeNode(int(value))
            while len(stack) > depth:
                stack.pop()
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.recoverFromPreorder,
            ("1-2--3--4-5--6--7",),
            "1,2,3,null,null,4,null,null,5,6,null,null,7,null,null",
        ),
        (
            solution.recoverFromPreorder,
            ("1-2--3---4-5--6---7",),
            "1,2,3,4,null,null,null,null,5,6,7,null,null,null,null",
        ),
        (
            solution.recoverFromPreorder,
            ("1-401--349---90--88",),
            "1,401,349,90,null,null,null,88,null,null,null",
        ),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = TreeNode.print_tree(func(*args))
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
