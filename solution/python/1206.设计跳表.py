#
# @lc app=leetcode.cn id=1206 lang=python3
# @lcpr version=30203
#
# [1206] 设计跳表
#

import os
import random
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Node:
    def __init__(self, value: int, level: int):
        self.value = value
        self.next = [None] * level


class Skiplist:
    MAX_LEVEL = 16

    def __init__(self):
        self.head = Node(-1, self.MAX_LEVEL)

    def _level(self) -> int:
        level = 1
        while level < self.MAX_LEVEL and random.getrandbits(1):
            level += 1
        return level

    def _predecessors(self, value: int) -> List[Node]:
        previous = [self.head] * self.MAX_LEVEL
        node = self.head
        for level in range(self.MAX_LEVEL - 1, -1, -1):
            while node.next[level] is not None and node.next[level].value < value:
                node = node.next[level]
            previous[level] = node
        return previous

    def search(self, target: int) -> bool:
        previous = self._predecessors(target)
        node = previous[0].next[0]
        return node is not None and node.value == target

    def add(self, num: int) -> None:
        previous = self._predecessors(num)
        node = Node(num, self._level())
        for level in range(len(node.next)):
            node.next[level] = previous[level].next[level]
            previous[level].next[level] = node

    def erase(self, num: int) -> bool:
        previous = self._predecessors(num)
        node = previous[0].next[0]
        if node is None or node.value != num:
            return False
        for level in range(len(node.next)):
            previous[level].next[level] = node.next[level]
        return True


# @lc code=end


if __name__ == "__main__":
    skiplist = Skiplist()
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    assert not skiplist.search(0)
    skiplist.add(4)
    assert skiplist.search(1)
    assert not skiplist.erase(0)
    assert skiplist.erase(1)
    assert not skiplist.search(1)
    skiplist.add(2)
    assert skiplist.erase(2)
    assert skiplist.search(2)
    print('第 1206 题 "设计跳表" 所有测试用例通过')
