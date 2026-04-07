#
# @lc app=leetcode.cn id=369 lang=python3
# @lcpr version=30203
#
# [369] 给单链表加一
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        not_nine = dummy
        curr = head
        while curr:
            if curr.val != 9:
                not_nine = curr
            curr = curr.next
        not_nine.val += 1
        curr = not_nine.next
        while curr:
            curr.val = 0
            curr = curr.next
        return dummy if dummy.val else dummy.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.plusOne, [ListNode.create_head([1, 2, 3])], "1 -> 2 -> 4"),
        (solution.plusOne, [ListNode.create_head([9, 9, 9])], "1 -> 0 -> 0 -> 0"),
        (solution.plusOne, [ListNode.create_head([0])], "1"),
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
# [1,2,3]\n
# @lcpr case=end

#
