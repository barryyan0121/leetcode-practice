#
# @lc app=leetcode.cn id=426 lang=python3
# @lcpr version=30203
#
# [426] 将二叉搜索树转化为排序的双向链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(self, val: int = 0, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        first = prev = None

        def dfs(node: Optional[Node]):
            nonlocal first, prev
            if not node:
                return
            dfs(node.left)
            if prev:
                prev.right = node
                node.left = prev
            else:
                first = node
            prev = node
            dfs(node.right)

        dfs(root)
        first.left = prev
        prev.right = first
        return first


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_bst(values: List[int]) -> Optional[Node]:
        if not values:
            return None
        root = Node(values[0])
        for v in values[1:]:
            cur = root
            while True:
                if v < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(v)
                        break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(v)
                        break
        return root

    def to_list(head: Optional[Node]) -> List[int]:
        if not head:
            return []
        res = []
        cur = head
        while True:
            res.append(cur.val)
            cur = cur.right
            if cur == head:
                break
        return res

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.treeToDoublyList, [build_bst([4, 2, 5, 1, 3])], [1, 2, 3, 4, 5]),
        (solution.treeToDoublyList, [build_bst([2, 1, 3])], [1, 2, 3]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = to_list(func(*args))
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
# [4,2,5,1,3]\n
# @lcpr case=end

#
