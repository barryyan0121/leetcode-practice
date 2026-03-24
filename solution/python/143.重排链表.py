#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30202
#
# [143] 重排链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first = head
        second = prev
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.reorderList,
            [ListNode.create_head([1, 2, 3, 4])],
            "1 -> 4 -> 2 -> 3",
        ),
        (
            solution.reorderList,
            [ListNode.create_head([1, 2, 3, 4, 5])],
            "1 -> 5 -> 2 -> 4 -> 3",
        ),
        (solution.reorderList, [ListNode.create_head([1, 2])], "1 -> 2"),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            head = args[0]
            func(*args)
            result = ListNode.print(head)
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
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#
