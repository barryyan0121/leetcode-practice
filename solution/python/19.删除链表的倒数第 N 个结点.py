#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30202
#
# [19] 删除链表的倒数第 N 个结点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.removeNthFromEnd,
            (ListNode.create_head([1, 2, 3, 4, 5]), 2),
            ListNode.create_head([1, 2, 3, 5]),
        ),
        (
            solution.removeNthFromEnd,
            (ListNode.create_head([1]), 1),
            None,
        ),
        (
            solution.removeNthFromEnd,
            (ListNode.create_head([1, 2]), 1),
            ListNode.create_head([1]),
        ),
        (
            solution.removeNthFromEnd,
            (ListNode.create_head([1, 2]), 2),
            ListNode.create_head([2]),
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
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#
