#
# @lc app=leetcode.cn id=99 lang=python3
# @lcpr version=30202
#
# [99] 恢复二叉搜索树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack = []
        current = root
        prev = None
        first = None
        second = None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()

            if prev is not None and current.val < prev.val:
                second = current
                if first is None:
                    first = prev
                else:
                    break

            prev = current
            current = current.right

        if first is not None and second is not None:
            first.val, second.val = second.val, first.val


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def serialize(root: Optional[TreeNode]) -> List[Optional[int]]:
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node is None:
                result.append(None)
                continue
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        while result and result[-1] is None:
            result.pop()
        return result

    tree1 = TreeNode.create_root([1, 3, None, None, 2])
    tree2 = TreeNode.create_root([3, 1, 4, None, None, 2])

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.recoverTree, (tree1,), [3, 1, None, None, 2]),
        (solution.recoverTree, (tree2,), [2, 1, 4, None, None, 3]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            func(*args)
            result = serialize(args[0])
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
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
# [1,3,null,null,2]\n
# @lcpr case=end
