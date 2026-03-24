#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30203
#
# [138] 随机链表的复制
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        current = head
        while current is not None:
            copy = Node(current.val, current.next)
            current.next = copy
            current = copy.next

        current = head
        while current is not None:
            if current.random is not None:
                current.next.random = current.random.next
            current = current.next.next

        dummy = Node(0)
        copy_tail = dummy
        current = head
        while current is not None:
            copy = current.next
            current.next = copy.next
            copy_tail.next = copy
            copy_tail = copy
            current = current.next

        return dummy.next


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build(values: List[List[Optional[int]]]) -> Optional[Node]:
        if not values:
            return None
        nodes = [Node(val) for val, _ in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        for i, (_, random_index) in enumerate(values):
            if random_index is not None:
                nodes[i].random = nodes[random_index]
        return nodes[0]

    def serialize(head: Optional[Node]) -> List[List[Optional[int]]]:
        nodes = []
        index_map = {}
        current = head
        index = 0
        while current is not None:
            index_map[current] = index
            nodes.append(current)
            current = current.next
            index += 1

        result = []
        for node in nodes:
            random_index = index_map[node.random] if node.random is not None else None
            result.append([node.val, random_index])
        return result

    def is_deep_copy(original: Optional[Node], copied: Optional[Node]) -> bool:
        while original is not None and copied is not None:
            if original is copied:
                return False
            original = original.next
            copied = copied.next
        return original is None and copied is None

    input1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    input2 = [[1, 1], [2, 1]]
    input3 = [[3, None], [3, 0], [3, None]]

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.copyRandomList, (build(input1),), input1),
        (solution.copyRandomList, (build(input2),), input2),
        (solution.copyRandomList, (build(input3),), input3),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            original = args[0]
            result = func(*args)
            assert serialize(result) == expected
            assert is_deep_copy(original, result)
            print(f"测试用例 {idx + 1} 通过: n = {expected}, result = {serialize(result)}")
        except AssertionError:
            all_passed = False
            actual = serialize(result) if result is not None else []
            print(
                f"测试用例 {idx + 1} 失败: n = {expected}, 期望 = {expected}, 实际 = {actual}"
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
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end
