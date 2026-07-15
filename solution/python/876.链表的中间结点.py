#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

import os
import sys
from typing import Optional

from common.node import ListNode


# @lc code=start
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.middleNode, (ListNode.create_head([1, 2, 3, 4, 5]),), [3, 4, 5]),
        (
            solution.middleNode,
            (ListNode.create_head([1, 2, 3, 4, 5, 6]),),
            [4, 5, 6],
        ),
        (solution.middleNode, (ListNode.create_head([1]),), [1]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        node = func(*args)
        result = []
        while node:
            result.append(node.val)
            node = node.next
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
