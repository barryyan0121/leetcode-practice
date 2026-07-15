#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#

import os
import sys
from typing import List, Optional

from common.node import ListNode


# @lc code=start
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        values = set(nums)
        answer = 0
        while head:
            if head.val in values and (not head.next or head.next.val not in values):
                answer += 1
            head = head.next
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numComponents, (ListNode.create_head([0, 1, 2, 3]), [0, 1, 3]), 2),
        (
            solution.numComponents,
            (ListNode.create_head([0, 1, 2, 3, 4]), [0, 3, 1, 4]),
            2,
        ),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
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
