#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#

import os
import sys
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.parents = deque([root])
        while self.parents[0].left and self.parents[0].right:
            node = self.parents.popleft()
            self.parents.append(node.left)
            self.parents.append(node.right)

    def insert(self, val: int) -> int:
        parent = self.parents[0]
        node = TreeNode(val)
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.parents.popleft()
            self.parents.append(parent.left)
            self.parents.append(parent.right)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root


# @lc code=end


def run_operations(values, inserts):
    tree = CBTInserter(TreeNode.create_root(values))
    parents = [tree.insert(value) for value in inserts]
    return parents, TreeNode.print_tree(tree.get_root())


if __name__ == "__main__":
    test_cases = [
        (
            run_operations,
            ([1, 2], [3, 4]),
            ([1, 2], "1,2,4,null,null,null,3,null,null"),
        ),
        (
            run_operations,
            ([1], [2, 3, 4]),
            ([1, 1, 2], "1,2,4,null,null,null,3,null,null"),
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
