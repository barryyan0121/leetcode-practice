#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30202
#
# [92] 反转链表 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_list(values: List[int]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        for value in values:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next

    def list_to_py(head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.reverseBetween, [build_list([1, 2, 3, 4, 5]), 2, 4], [1, 4, 3, 2, 5]),
        (solution.reverseBetween, [build_list([5]), 1, 1], [5]),
        (solution.reverseBetween, [build_list([3, 5]), 1, 2], [5, 3]),
        (solution.reverseBetween, [build_list([1, 2, 3, 4, 5]), 1, 5], [5, 4, 3, 2, 1]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result = list_to_py(result)
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
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#
