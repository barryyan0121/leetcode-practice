#
# @lc app=leetcode.cn id=428 lang=python3
# @lcpr version=30203
#
# [428] 序列化和反序列化N叉树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children if children is not None else []


# @lc code=start
class Codec:
    def serialize(self, root: Optional["Node"]) -> str:
        if not root:
            return "#"
        res = []

        def dfs(node: Node):
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for child in node.children:
                dfs(child)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional["Node"]:
        if not data or data == "#":
            return None
        vals = iter(data.split(","))

        def dfs() -> Node:
            val = int(next(vals))
            cnt = int(next(vals))
            node = Node(val, [])
            for _ in range(cnt):
                node.children.append(dfs())
            return node

        return dfs()


# @lc code=end


if __name__ == "__main__":
    codec = Codec()

    def build_tree() -> Node:
        return Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

    def same(root: Optional[Node]) -> bool:
        return codec.serialize(codec.deserialize(codec.serialize(root))) == codec.serialize(root)

    # 测试用例 (func, args, result)
    test_cases = [
        (same, [build_tree()], True),
        (same, [None], True),
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
# [1,[3,[5,6],2,4]]\n
# @lcpr case=end

#
