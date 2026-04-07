#
# @lc app=leetcode.cn id=203 lang=python3
# @lcpr version=30202
#
# [203] 移除链表元素
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.removeElements, [ListNode.create_head([1, 2, 6, 3, 4, 5, 6]), 6], "1 -> 2 -> 3 -> 4 -> 5"),
        (solution.removeElements, [ListNode.create_head([]), 1], ""),
        (solution.removeElements, [ListNode.create_head([7, 7, 7, 7]), 7], ""),
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
# [1,2,6,3,4,5,6]\n6\n
# @lcpr case=end

#
