#
# @lc app=leetcode.cn id=328 lang=python3
# @lcpr version=30203
#
# [328] 奇偶链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.oddEvenList, [ListNode.create_head([1, 2, 3, 4, 5])], "1 -> 3 -> 5 -> 2 -> 4"),
        (solution.oddEvenList, [ListNode.create_head([2, 1, 3, 5, 6, 4, 7])], "2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4"),
        (solution.oddEvenList, [ListNode.create_head([1])], "1"),
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
# [1,2,3,4,5]\n
# @lcpr case=end

#
