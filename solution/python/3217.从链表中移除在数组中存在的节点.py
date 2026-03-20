#
# @lc app=leetcode.cn id=3217 lang=python3
# @lcpr version=30300
#
# [3217] 从链表中移除在数组中存在的节点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        nums_set = set(nums)
        while curr.next:
            if curr.next.val in nums_set:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.modifiedList,
            ([1, 2, 3], ListNode.create_head([1, 2, 3, 4, 5])),
            ListNode.create_head([4, 5]),
        ),
        (
            solution.modifiedList,
            ([1], ListNode.create_head([1, 2, 1, 2, 1, 2])),
            ListNode.create_head([2, 2, 2]),
        ),
        (
            solution.modifiedList,
            ([5], ListNode.create_head([1, 2, 3, 4])),
            ListNode.create_head([1, 2, 3, 4]),
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
# [1,2,3]\n[1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1,2,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [5]\n[1,2,3,4]\n
# @lcpr case=end

#
