#
# @lc app=leetcode.cn id=1188 lang=python3
#
# [1188] 设计有限阻塞队列
#

# @lc code=start
from collections import deque
from threading import Condition


class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.condition = Condition()

    def enqueue(self, element: int) -> None:
        with self.condition:
            while len(self.queue) == self.capacity:
                self.condition.wait()
            self.queue.append(element)
            self.condition.notify()

    def dequeue(self) -> int:
        with self.condition:
            while not self.queue:
                self.condition.wait()
            element = self.queue.popleft()
            self.condition.notify()
            return element

    def size(self) -> int:
        with self.condition:
            return len(self.queue)


# Your BoundedBlockingQueue object will be instantiated and called as such:
# obj = BoundedBlockingQueue(capacity)
# obj.enqueue(element)
# param_2 = obj.dequeue()
# param_3 = obj.size()
# @lc code=end


if __name__ == "__main__":
    test_cases = [(2, [1, 2], [1, 2])]
    for index, (capacity, values, expected) in enumerate(test_cases):
        queue = BoundedBlockingQueue(capacity)
        for value in values:
            queue.enqueue(value)
        assert [queue.dequeue() for _ in values] == expected, index
