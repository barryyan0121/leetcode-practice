#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30202
#
# [24] 两两交换链表中的节点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second
            prev = first

        return dummy.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.swapPairs,
            (ListNode.create_head([1, 2, 3, 4]),),
            ListNode.create_head([2, 1, 4, 3]),
        ),
        (
            solution.swapPairs,
            (ListNode.create_head([]),),
            None,
        ),
        (
            solution.swapPairs,
            (ListNode.create_head([1]),),
            ListNode.create_head([1]),
        ),
        (
            solution.swapPairs,
            (ListNode.create_head([1, 2, 3]),),
            ListNode.create_head([2, 1, 3]),
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
# [1,2,3,4]\n
# @lcpr case=end

#
