#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30202
#
# [61] 旋转链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import ListNode


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        tail.next = head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_list = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([1], 0, [1]),
    ]
    test_cases = []
    for head_vals, k, expected_vals in test_list:
        head = ListNode.create_head(head_vals)
        expected = ListNode.create_head(expected_vals)
        test_cases.append((solution.rotateRight, (head, k), expected))

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            args = (ListNode.print(args[0]), args[1])
            result = ListNode.print(result)
            expected = ListNode.print(expected)
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
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#
