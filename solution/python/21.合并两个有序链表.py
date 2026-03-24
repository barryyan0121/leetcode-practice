#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30202
#
# [21] 合并两个有序链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.mergeTwoLists,
            (ListNode.create_head([1, 2, 4]), ListNode.create_head([1, 3, 4])),
            ListNode.create_head([1, 1, 2, 3, 4, 4]),
        ),
        (
            solution.mergeTwoLists,
            (None, None),
            None,
        ),
        (
            solution.mergeTwoLists,
            (None, ListNode.create_head([0])),
            ListNode.create_head([0]),
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert ListNode.print(result) == ListNode.print(expected)
            print(
                f"测试用例 {idx + 1} 通过: n = {args}, result = {ListNode.print(result)}"
            )
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {ListNode.print(expected)}, 实际 = {ListNode.print(result)}"
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
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

#
