# @lc app=leetcode.cn id=2502 lang=python3


class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.max_free = [0] * (4 * n)
        self.prefix = [0] * (4 * n)
        self.suffix = [0] * (4 * n)
        self.lazy = [-1] * (4 * n)
        self.owners = {}
        self._build(1, 0, n - 1)

    def _build(self, node: int, left: int, right: int) -> None:
        length = right - left + 1
        self.max_free[node] = self.prefix[node] = self.suffix[node] = length
        if left < right:
            middle = (left + right) // 2
            self._build(node * 2, left, middle)
            self._build(node * 2 + 1, middle + 1, right)

    def _apply(self, node: int, length: int, free: bool) -> None:
        value = length if free else 0
        self.max_free[node] = self.prefix[node] = self.suffix[node] = value
        self.lazy[node] = int(free)

    def _push(self, node: int, left: int, right: int) -> None:
        if self.lazy[node] == -1 or left == right:
            return
        middle = (left + right) // 2
        self._apply(node * 2, middle - left + 1, bool(self.lazy[node]))
        self._apply(node * 2 + 1, right - middle, bool(self.lazy[node]))
        self.lazy[node] = -1

    def _pull(self, node: int, left: int, right: int) -> None:
        middle = (left + right) // 2
        first, second = node * 2, node * 2 + 1
        left_len, right_len = middle - left + 1, right - middle
        self.prefix[node] = (
            left_len + self.prefix[second]
            if self.prefix[first] == left_len
            else self.prefix[first]
        )
        self.suffix[node] = (
            right_len + self.suffix[first]
            if self.suffix[second] == right_len
            else self.suffix[second]
        )
        self.max_free[node] = max(
            self.max_free[first],
            self.max_free[second],
            self.suffix[first] + self.prefix[second],
        )

    def _update(
        self, node: int, left: int, right: int, ql: int, qr: int, free: bool
    ) -> None:
        if ql <= left and right <= qr:
            self._apply(node, right - left + 1, free)
            return
        self._push(node, left, right)
        middle = (left + right) // 2
        if ql <= middle:
            self._update(node * 2, left, middle, ql, qr, free)
        if qr > middle:
            self._update(node * 2 + 1, middle + 1, right, ql, qr, free)
        self._pull(node, left, right)

    def _first_fit(self, node: int, left: int, right: int, size: int) -> int:
        if left == right:
            return left
        self._push(node, left, right)
        middle = (left + right) // 2
        first, second = node * 2, node * 2 + 1
        if self.max_free[first] >= size:
            return self._first_fit(first, left, middle, size)
        if self.suffix[first] + self.prefix[second] >= size:
            return middle - self.suffix[first] + 1
        return self._first_fit(second, middle + 1, right, size)

    def allocate(self, size: int, mID: int) -> int:
        if self.max_free[1] < size:
            return -1
        start = self._first_fit(1, 0, self.n - 1, size)
        self._update(1, 0, self.n - 1, start, start + size - 1, False)
        self.owners.setdefault(mID, []).append((start, start + size - 1))
        return start

    def freeMemory(self, mID: int) -> int:
        released = 0
        for start, end in self.owners.pop(mID, []):
            self._update(1, 0, self.n - 1, start, end, True)
            released += end - start + 1
        return released


if __name__ == "__main__":
    allocator = Allocator(10)
    test_cases = [
        (allocator.allocate, (1, 1), 0),
        (allocator.allocate, (1, 2), 1),
        (allocator.freeMemory, (1,), 1),
        (allocator.allocate, (3, 2), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2502 题 "设计内存分配器" 所有测试用例通过')
