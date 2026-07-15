#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

import os
import sys
from typing import *
from common.node import *


# @lc code=start
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        size, extra = divmod(length, k)
        answer = []
        node = head
        for part in range(k):
            answer.append(node)
            for _ in range(size + (part < extra) - 1):
                if node:
                    node = node.next
            if node:
                node.next, node = None, node.next
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.splitListToParts,
            (ListNode.create_head([1, 2, 3]), 5),
            ["1", "2", "3", "", ""],
        ),
        (
            solution.splitListToParts,
            (ListNode.create_head(list(range(1, 11))), 3),
            ["1 -> 2 -> 3 -> 4", "5 -> 6 -> 7", "8 -> 9 -> 10"],
        ),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = [ListNode.print(node) if node else "" for node in func(*args)]
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
