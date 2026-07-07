#
# @lc app=leetcode.cn id=641 lang=python3
# @lcpr version=30203
#
# [641] 设计循环双端队列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class MyCircularDeque:
    def __init__(self, k: int):
        self.data = [0] * k
        self.front = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[(self.front + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.data[(self.front + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# @lc code=end


if __name__ == "__main__":
    deque_obj = MyCircularDeque(3)
    test_cases = [
        (deque_obj.insertLast, (1,), True),
        (deque_obj.insertLast, (2,), True),
        (deque_obj.insertFront, (3,), True),
        (deque_obj.insertFront, (4,), False),
        (deque_obj.getRear, tuple(), 2),
        (deque_obj.isFull, tuple(), True),
        (deque_obj.deleteLast, tuple(), True),
        (deque_obj.insertFront, (4,), True),
        (deque_obj.getFront, tuple(), 4),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)

