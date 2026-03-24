#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30202
#
# [86] 分隔链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before = before_dummy
        after = after_dummy

        while head:
            nxt = head.next
            head.next = None
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = nxt

        before.next = after_dummy.next
        return before_dummy.next
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.partition,
            [ListNode.create_head([1, 4, 3, 2, 5, 2]), 3],
            "1 -> 2 -> 2 -> 4 -> 3 -> 5",
        ),
        (
            solution.partition,
            [ListNode.create_head([2, 1]), 2],
            "1 -> 2",
        ),
        (solution.partition, [None, 1], ""),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result_text = ListNode.print(result)
            assert result_text == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result_text}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result_text}"
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
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#
