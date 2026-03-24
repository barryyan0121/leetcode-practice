#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30203
#
# [160] 相交链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    shared1 = ListNode.create_head([8, 4, 5])
    headA1 = ListNode.create_head([4, 1])
    tail = headA1
    while tail.next:
        tail = tail.next
    tail.next = shared1
    headB1 = ListNode.create_head([5, 6, 1])
    tail = headB1
    while tail.next:
        tail = tail.next
    tail.next = shared1

    shared2 = ListNode.create_head([2, 4])
    headA2 = ListNode.create_head([1, 9, 1])
    tail = headA2
    while tail.next:
        tail = tail.next
    tail.next = shared2
    headB2 = ListNode.create_head([3])
    headB2.next = shared2

    test_cases = [
        (solution.getIntersectionNode, (headA1, headB1), shared1),
        (solution.getIntersectionNode, (headA2, headB2), shared2),
        (solution.getIntersectionNode, (None, None), None),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result is expected
            result_str = ListNode.print(result) if result else ""
            expected_str = ListNode.print(expected) if expected else ""
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result_str}")
        except AssertionError:
            all_passed = False
            result_str = ListNode.print(result) if result else ""
            expected_str = ListNode.print(expected) if expected else ""
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected_str}, 实际 = {result_str}"
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
# [4,1,8,4,5]\n[5,6,1,8,4,5]\n
# @lcpr case=end
