#
# @lc app=leetcode.cn id=431 lang=python3
# @lcpr version=30203
#
# [431] 将N叉树编码为二叉树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children if children is not None else []


# @lc code=start
class Codec:
    def encode(self, root: Optional[Node]) -> Optional[TreeNode]:
        if not root:
            return None
        b_root = TreeNode(root.val)
        if root.children:
            b_root.left = self.encode(root.children[0])
            cur = b_root.left
            for child in root.children[1:]:
                cur.right = self.encode(child)
                cur = cur.right
        return b_root

    def decode(self, data: Optional[TreeNode]) -> Optional[Node]:
        if not data:
            return None
        root = Node(data.val, [])
        cur = data.left
        while cur:
            root.children.append(self.decode(cur))
            cur = cur.right
        return root


# @lc code=end


if __name__ == "__main__":
    codec = Codec()

    def build():
        return Node(1, [Node(2), Node(3, [Node(5), Node(6)]), Node(4)])

    def serialize(node: Optional[Node]) -> Tuple:
        if not node:
            return ()
        return (node.val, tuple(serialize(c) for c in node.children))

    def roundtrip(root: Optional[Node]) -> Tuple:
        return serialize(codec.decode(codec.encode(root)))

    # 测试用例 (func, args, result)
    test_cases = [
        (roundtrip, [build()], serialize(build())),
        (roundtrip, [None], ()),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
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
# [1,[2,3,4,[5,6]]]\n
# @lcpr case=end

#
