#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30203
#
# [141] 环形链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import ListNode


# @lc code=start
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_cycle(nums: List[int], pos: int) -> Optional[ListNode]:
        head = ListNode.create_head(nums)
        if head is None or pos < 0:
            return head

        current = head
        cycle_node = None
        index = 0
        tail = None
        while current is not None:
            if index == pos:
                cycle_node = current
            tail = current
            current = current.next
            index += 1
        tail.next = cycle_node
        return head

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.hasCycle, (build_cycle([3, 2, 0, -4], 1),), True),
        (solution.hasCycle, (build_cycle([1, 2], 0),), True),
        (solution.hasCycle, (build_cycle([1], -1),), False),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = ({expected},), result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = ({expected},), 期望 = {expected}, 实际 = {result}"
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
# [3,2,0,-4]\n1\n
# @lcpr case=end
