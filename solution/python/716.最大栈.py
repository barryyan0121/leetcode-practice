#
# @lc app=leetcode.cn id=716 lang=python3
#
# [716] 最大栈
#


# @lc code=start
import heapq


class _Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None
        self.active = True


class MaxStack:
    def __init__(self):
        self.head, self.tail = _Node(0), _Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.heap = []
        self.by_value = {}

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.active = False
        bucket = self.by_value[node.value]
        while bucket and not bucket[-1].active:
            bucket.pop()

    def push(self, x: int) -> None:
        node = _Node(x)
        node.prev, node.next = self.tail.prev, self.tail
        node.prev.next = node.next.prev = node
        heapq.heappush(self.heap, -x)
        self.by_value.setdefault(x, []).append(node)

    def pop(self) -> int:
        node = self.tail.prev
        self._remove(node)
        return node.value

    def top(self) -> int:
        return self.tail.prev.value

    def peekMax(self) -> int:
        while (
            not self.by_value[-self.heap[0]]
            or not self.by_value[-self.heap[0]][-1].active
        ):
            heapq.heappop(self.heap)
        return -self.heap[0]

    def popMax(self) -> int:
        value = self.peekMax()
        node = self.by_value[value].pop()
        node.prev.next, node.next.prev = node.next, node.prev
        node.active = False
        heapq.heappop(self.heap)
        return value

if __name__ == "__main__":
    stack = MaxStack()
    for value in (5, 1, 5): stack.push(value)
    assert stack.top() == 5 and stack.popMax() == 5
    assert stack.top() == 1 and stack.peekMax() == 5


if __name__ == "__main__":
    s = MaxStack()
    s.push(5)
    s.push(1)
    s.push(5)
    assert s.top() == 5
    assert s.popMax() == 5
    assert s.top() == 1
    assert s.peekMax() == 5
    assert s.pop() == 1
