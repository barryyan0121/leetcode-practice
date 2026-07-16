#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

import os
import sys
from typing import List

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import ListNode


# @lc code=start
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result = []
        stack = []
        while head:
            while stack and stack[-1][1] < head.val:
                index, _ = stack.pop()
                result[index] = head.val
            stack.append((len(result), head.val))
            result.append(0)
            head = head.next
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.nextLargerNodes, (ListNode.create_head([2, 1, 5]),), [5, 5, 0]),
        (
            solution.nextLargerNodes,
            (ListNode.create_head([2, 7, 4, 3, 5]),),
            [7, 0, 5, 5, 0],
        ),
        (solution.nextLargerNodes, (ListNode.create_head([1]),), [0]),
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
