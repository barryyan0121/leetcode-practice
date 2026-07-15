#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

import os
import sys


# @lc code=start
class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.head.next
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(index, 0)
        previous = self.head
        for _ in range(index):
            previous = previous.next
        previous.next = Node(val, previous.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        previous = self.head
        for _ in range(index):
            previous = previous.next
        previous.next = previous.next.next
        self.size -= 1


# @lc code=end


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    test_cases = [
        (obj.get, (1,), 2),
        (obj.deleteAtIndex, (1,), None),
        (obj.get, (1,), 3),
        (obj.get, (3,), -1),
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
