#
# @lc app=leetcode.cn id=445 lang=python3
# @lcpr version=30203
#
# [445] 两数相加 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import ListNode


# @lc code=start
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while stack1 or stack2 or carry:
            total = carry
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
            node = ListNode(total % 10)
            node.next = head
            head = node
            carry = total // 10

        return head


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.addTwoNumbers,
            (ListNode.create_head([7, 2, 4, 3]), ListNode.create_head([5, 6, 4])),
            "7 -> 8 -> 0 -> 7",
        ),
        (
            solution.addTwoNumbers,
            (ListNode.create_head([2, 4, 3]), ListNode.create_head([5, 6, 4])),
            "8 -> 0 -> 7",
        ),
        (
            solution.addTwoNumbers,
            (ListNode.create_head([0]), ListNode.create_head([0])),
            "0",
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            printed = ListNode.print(result)
            assert printed == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {printed}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {printed}"
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
# [7,2,4,3]\n[5,6,4]\n
# @lcpr case=end
