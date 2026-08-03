# @lc app=leetcode.cn id=2502 lang=python3


class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        start = 0
        while start + size <= len(self.memory):
            if all(value == 0 for value in self.memory[start : start + size]):
                self.memory[start : start + size] = [mID] * size
                return start
            start += 1
        return -1

    def free(self, mID: int) -> int:
        released = 0
        for index, value in enumerate(self.memory):
            if value == mID:
                self.memory[index] = 0
                released += 1
        return released


if __name__ == "__main__":
    allocator = Allocator(10)
    test_cases = [
        (allocator.allocate, (1, 1), 0),
        (allocator.allocate, (1, 2), 1),
        (allocator.free, (1,), 1),
        (allocator.allocate, (3, 2), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2502 题 "设计内存分配器" 所有测试用例通过')
