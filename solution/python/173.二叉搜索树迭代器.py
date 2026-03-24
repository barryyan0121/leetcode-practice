#
# @lc app=leetcode.cn id=173 lang=python3
# @lcpr version=30203
#
# [173] 二叉搜索树迭代器
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]) -> None:
        while node is not None:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# @lc code=end


if __name__ == "__main__":
    def run_operations(ops: List[str], values: List[List[Optional[int]]]) -> List[Optional[bool]]:
        iterator = None
        result = []

        for op, value in zip(ops, values):
            if op == "BSTIterator":
                iterator = BSTIterator(TreeNode.create_root(value))
                result.append(None)
            elif op == "next":
                result.append(iterator.next())
            elif op == "hasNext":
                result.append(iterator.hasNext())
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
                [[7, 3, 15, None, None, 9, 20], [], [], [], [], [], [], [], [], []],
            ),
            [None, 3, 7, True, 9, True, 15, True, 20, False],
        ),
        (
            run_operations,
            (
                ["BSTIterator", "hasNext", "next", "hasNext"],
                [[1], [], [], []],
            ),
            [None, True, 1, False],
        ),
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
# ["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[7,3,15,null,null,9,20],[],[],[],[],[],[],[],[],[]]\n
# @lcpr case=end
