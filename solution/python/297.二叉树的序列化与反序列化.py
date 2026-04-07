#
# @lc app=leetcode.cn id=297 lang=python3
# @lcpr version=30203
#
# [297] 二叉树的序列化与反序列化
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        res = []
        queue = [root]
        for node in queue:
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")
        while res and res[-1] == "#":
            res.pop()
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == "#":
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue = [root]
        idx = 1
        for node in queue:
            if idx >= len(vals):
                break
            if vals[idx] != "#":
                node.left = TreeNode(int(vals[idx]))
                queue.append(node.left)
            idx += 1
            if idx >= len(vals):
                break
            if vals[idx] != "#":
                node.right = TreeNode(int(vals[idx]))
                queue.append(node.right)
            idx += 1
        return root


# @lc code=start
# 这里的 Codec 已经定义在上面
# @lc code=end


if __name__ == "__main__":
    codec = Codec()

    def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = [root]
        idx = 1
        for node in queue:
            if idx >= len(values):
                break
            left_val = values[idx]
            idx += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            if idx >= len(values):
                break
            right_val = values[idx]
            idx += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        return root

    def serialize_roundtrip(root):
        return codec.serialize(codec.deserialize(codec.serialize(root)))

    # 测试用例 (func, args, result)
    test_cases = [
        (serialize_roundtrip, [build_tree([1, 2, 3, None, None, 4, 5])], codec.serialize(build_tree([1, 2, 3, None, None, 4, 5]))),
        (serialize_roundtrip, [None], "#"),
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
# [1,2,3,null,null,4,5]\n
# @lcpr case=end

#
