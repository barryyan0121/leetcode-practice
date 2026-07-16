#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#

import os
import sys
from typing import List

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        index = 0

        def build(bound):
            nonlocal index
            if index == len(preorder) or preorder[index] > bound:
                return None
            value = preorder[index]
            index += 1
            node = TreeNode(value)
            node.left = build(value)
            node.right = build(bound)
            return node

        return build(float("inf"))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.bstFromPreorder,
            ([8, 5, 1, 7, 10, 12],),
            "8,5,1,null,null,7,null,null,10,null,12,null,null",
        ),
        (solution.bstFromPreorder, ([1, 3],), "1,null,3,null,null"),
        (solution.bstFromPreorder, ([2, 1],), "2,1,null,null,null"),
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
