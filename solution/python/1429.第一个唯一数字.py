# @lc app=leetcode.cn id=1429 lang=python3

from collections import Counter, deque
from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = deque(nums)
        self.counts = Counter(nums)

    def showFirstUnique(self) -> int:
        while self.queue and self.counts[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.counts[value] += 1


if __name__ == "__main__":

    def run(nums, operations):
        first_unique = FirstUnique(nums)
        result = []
        for operation, value in operations:
            if operation == "show":
                result.append(first_unique.showFirstUnique())
            else:
                first_unique.add(value)
        return result

    test_cases = [
        (
            run,
            (
                [2, 3, 5],
                [
                    ("show", None),
                    ("add", 5),
                    ("show", None),
                    ("add", 2),
                    ("show", None),
                    ("add", 3),
                    ("show", None),
                ],
            ),
            [2, 2, 3, -1],
        ),
        (
            run,
            (
                [7, 7, 7, 7, 7, 7],
                [
                    ("show", None),
                    ("add", 7),
                    ("add", 3),
                    ("show", None),
                    ("add", 3),
                    ("show", None),
                    ("add", 7),
                    ("show", None),
                    ("add", 17),
                    ("show", None),
                ],
            ),
            [-1, 3, -1, -1, 17],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1429 题 "第一个唯一数字" 所有测试用例通过')
