#
# @lc app=leetcode.cn id=382 lang=python3
# @lcpr version=30203
#
# [382] 链表随机节点
#

import sys
import os
import random

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import ListNode


# @lc code=start
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = self.head.val
        current = self.head.next
        count = 2

        while current is not None:
            if random.randrange(count) == 0:
                result = current.val
            current = current.next
            count += 1

        return result


# @lc code=end


if __name__ == "__main__":

    def run_operations(ops: List[str], values: List[List[int]]) -> List[Any]:
        random.seed(0)
        obj = None
        result = []

        for op, value in zip(ops, values):
            if op == "Solution":
                obj = Solution(ListNode.create_head(value))
                result.append(None)
            elif op == "getRandom":
                result.append(obj.getRandom())
        return result

    def check_result(result: List[Any], expected: List[Any]) -> bool:
        if len(result) != len(expected):
            return False
        for actual, target in zip(result, expected):
            if isinstance(target, set):
                if actual not in target:
                    return False
            elif actual != target:
                return False
        return True

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_operations,
            (
                ["Solution", "getRandom", "getRandom", "getRandom"],
                [[1, 2, 3], [], [], []],
            ),
            [None, {1, 2, 3}, {1, 2, 3}, {1, 2, 3}],
        ),
        (
            run_operations,
            (
                ["Solution", "getRandom"],
                [[7], []],
            ),
            [None, 7],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert check_result(result, expected)
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
# ["Solution","getRandom"]\n[[1,2,3],[]]\n
# @lcpr case=end
