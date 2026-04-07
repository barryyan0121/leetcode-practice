#
# @lc app=leetcode.cn id=449 lang=python3
# @lcpr version=30203
#
# [449] 序列化和反序列化二叉搜索树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []

        def preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = list(map(int, data.split(",")))
        index = 0

        def build(lower: int, upper: int) -> Optional[TreeNode]:
            nonlocal index
            if index == len(values) or not (lower < values[index] < upper):
                return None
            value = values[index]
            index += 1
            node = TreeNode(value)
            node.left = build(lower, value)
            node.right = build(value, upper)
            return node

        return build(float("-inf"), float("inf"))


# @lc code=end


if __name__ == "__main__":
    codec = Codec()

    def round_trip(values: List[Optional[int]]) -> str:
        root = TreeNode.create_root(values)
        data = codec.serialize(root)
        restored = codec.deserialize(data)
        return TreeNode.print_tree(restored)

    test_cases = [
        (round_trip, ([2, 1, 3],), "2,1,null,null,3,null,null"),
        (round_trip, ([5, 3, 6, 2, 4, None, 7],), "5,3,2,null,null,4,null,null,6,null,7,null,null"),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

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
# [2,1,3]\n
# @lcpr case=end
