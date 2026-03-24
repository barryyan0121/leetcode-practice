#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            duplicate = False
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                duplicate = True

            if duplicate:
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        return dummy.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_list = [
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
        ([1, 1], []),
    ]
    test_cases = []
    for head_vals, expected_vals in test_list:
        head = ListNode.create_head(head_vals)
        expected = ListNode.create_head(expected_vals)
        test_cases.append((solution.deleteDuplicates, (head,), expected))

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result = ListNode.print(result) if result else ""
            expected = ListNode.print(expected) if expected else ""
            args = (ListNode.print(args[0]) if args[0] else "",)
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
# [1,2,3,3,4,4,5]\n
# @lcpr case=end
