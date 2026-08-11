#
# @lc app=leetcode.cn id=2286 lang=python3
# @lcpr version=30203
#
# [2286] 以组为单位订音乐会的门票
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.remaining = [m] * n
        self.max_tree = [m] * (4 * n)
        self.sum_tree = [0] * (4 * n)
        self._build(1, 0, n - 1)
        self.next_row = 0

    def _build(self, node: int, left: int, right: int) -> None:
        self.sum_tree[node] = (right - left + 1) * self.m
        if left == right:
            return
        middle = (left + right) // 2
        self._build(node * 2, left, middle)
        self._build(node * 2 + 1, middle + 1, right)

    def _update(self, node: int, left: int, right: int, index: int) -> None:
        if left == right:
            self.max_tree[node] = self.sum_tree[node] = self.remaining[index]
            return
        middle = (left + right) // 2
        if index <= middle:
            self._update(node * 2, left, middle, index)
        else:
            self._update(node * 2 + 1, middle + 1, right, index)
        self.max_tree[node] = max(self.max_tree[node * 2], self.max_tree[node * 2 + 1])
        self.sum_tree[node] = self.sum_tree[node * 2] + self.sum_tree[node * 2 + 1]

    def _first(self, node: int, left: int, right: int, limit: int, seats: int) -> int:
        if left > limit or self.max_tree[node] < seats:
            return -1
        if left == right:
            return left
        middle = (left + right) // 2
        result = self._first(node * 2, left, middle, limit, seats)
        if result != -1:
            return result
        return self._first(node * 2 + 1, middle + 1, right, limit, seats)

    def _sum(self, node: int, left: int, right: int, limit: int) -> int:
        if left > limit:
            return 0
        if right <= limit:
            return self.sum_tree[node]
        middle = (left + right) // 2
        return self._sum(node * 2, left, middle, limit) + self._sum(
            node * 2 + 1, middle + 1, right, limit
        )

    def gather(self, k: int, maxRow: int) -> List[int]:
        row = self._first(1, 0, self.n - 1, maxRow, k)
        if row == -1:
            return []
        start = self.m - self.remaining[row]
        self.remaining[row] -= k
        self._update(1, 0, self.n - 1, row)
        return [row, start]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self._sum(1, 0, self.n - 1, maxRow) < k:
            return False
        while k:
            while self.next_row <= maxRow and self.remaining[self.next_row] == 0:
                self.next_row += 1
            take = min(k, self.remaining[self.next_row])
            self.remaining[self.next_row] -= take
            k -= take
            self._update(1, 0, self.n - 1, self.next_row)
        return True


# @lc code=end


if __name__ == "__main__":
    book = BookMyShow(2, 5)
    assert book.gather(4, 0) == [0, 0]
    assert book.gather(2, 0) == []
    assert book.scatter(5, 1)
    assert not book.scatter(5, 1)
    print('第 2286 题 "以组为单位订音乐会的门票" 所有测试用例通过')
