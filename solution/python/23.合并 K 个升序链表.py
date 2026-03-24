#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30202
#
# [23] 合并 K 个升序链表
#

import sys
import os
import heapq

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.mergeKLists,
            (
                [
                    ListNode.create_head([1, 4, 5]),
                    ListNode.create_head([1, 3, 4]),
                    ListNode.create_head([2, 6]),
                ],
            ),
            ListNode.create_head([1, 1, 2, 3, 4, 4, 5, 6]),
        ),
        (solution.mergeKLists, ([],), None),
        (solution.mergeKLists, ([None],), None),
        (
            solution.mergeKLists,
            ([ListNode.create_head([2]), ListNode.create_head([1])],),
            ListNode.create_head([1, 2]),
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
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

#
