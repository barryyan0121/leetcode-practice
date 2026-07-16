#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

import os
import sys
from typing import List, Optional

from common.node import TreeNode


# @lc code=start
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        post_index = 0
        for value in preorder[1:]:
            while stack[-1].val == postorder[post_index]:
                stack.pop()
                post_index += 1
            node = TreeNode(value)
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.constructFromPrePost,
            ([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]),
            "1,2,4,null,null,5,null,null,3,6,null,null,7,null,null",
        ),
        (solution.constructFromPrePost, ([1], [1]), "1,null,null"),
        (
            solution.constructFromPrePost,
            ([1, 2, 3], [3, 2, 1]),
            "1,2,3,null,null,null,null",
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
