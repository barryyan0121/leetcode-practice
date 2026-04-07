#
# @lc app=leetcode.cn id=430 lang=python3
# @lcpr version=30203
#
# [430] 扁平化多级双向链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(
        self,
        val: int,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None,
        child: Optional["Node"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# @lc code=start
class Solution:
    def flatten(self, head: Optional["Node"]) -> Optional["Node"]:
        if not head:
            return head
        stack = [head]
        prev = None
        while stack:
            node = stack.pop()
            if prev:
                prev.next = node
                node.prev = prev
            while node:
                if node.next:
                    stack.append(node.next)
                if node.child:
                    stack.append(node.child)
                    node.child = None
                prev = node
                if stack:
                    node = stack.pop()
                    prev.next = node
                    node.prev = prev
                else:
                    node = None
        return head


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build():
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n8 = Node(8)
        n9 = Node(9)
        n10 = Node(10)
        n11 = Node(11)
        n12 = Node(12)
        n1.next = n2; n2.prev = n1
        n2.next = n3; n3.prev = n2
        n3.next = n4; n4.prev = n3
        n3.child = n7
        n7.next = n8; n8.prev = n7
        n8.next = n9; n9.prev = n8
        n9.next = n10; n10.prev = n9
        n8.child = n11
        n11.next = n12; n12.prev = n11
        return n1

    def to_list(head: Optional[Node]) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.flatten, [build()], [1, 2, 3, 7, 8, 11, 12, 9, 10, 4]),
        (solution.flatten, [None], []),
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
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]\n
# @lcpr case=end

#
