#
# @lc app=leetcode.cn id=237 lang=python3
# @lcpr version=30203
#
# [237] 删除链表中的节点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    # 测试用例 (func, args, result)
    def build_case(values: List[int], idx: int):
        head = ListNode.create_head(values)
        target = head
        for _ in range(idx):
            target = target.next
        return head, target

    head1, node1 = build_case([4, 5, 1, 9], 1)
    head2, node2 = build_case([1, 2, 3, 4], 2)

    test_cases = [
        (solution.deleteNode, (node1,), "4 -> 1 -> 9"),
        (solution.deleteNode, (node2,), "1 -> 2 -> 4"),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            func(*args)
            head = head1 if idx == 0 else head2
            result = ListNode.print(head)
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
# node = [4,5,1,9], delete 5\n
# @lcpr case=end
