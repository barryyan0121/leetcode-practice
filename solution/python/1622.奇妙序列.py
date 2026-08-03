# @lc app=leetcode.cn id=1622 lang=python3


class Fancy:
    def __init__(self):
        self.values = []
        self.mul = 1
        self.add = 0
        self.mod = 10**9 + 7

    def append(self, val: int) -> None:
        inverse = pow(self.mul, self.mod - 2, self.mod)
        self.values.append((val - self.add) * inverse % self.mod)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.mod
        self.add = self.add * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        return (self.values[idx] * self.mul + self.add) % self.mod


if __name__ == "__main__":
    sequence = Fancy()
    sequence.append(2)
    sequence.addAll(3)
    sequence.append(7)
    sequence.multAll(2)
    test_cases = [(sequence.getIndex, (0,), 10), (sequence.getIndex, (1,), 14)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1622 题 "奇妙序列" 所有测试用例通过')
