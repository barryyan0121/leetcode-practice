# @lc app=leetcode.cn id=1381 lang=python3
class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size, self.stack = maxSize, []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        for index in range(min(k, len(self.stack))):
            self.stack[index] += val


if __name__ == "__main__":
    test_cases = ["stack"]
    for _, _case in enumerate(test_cases):
        pass
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.increment(5, 100)
    assert [stack.pop(), stack.pop(), stack.pop(), stack.pop()] == [103, 102, 101, -1]
    print('第 1381 题 "设计一个支持增量操作的栈" 所有测试用例通过')
