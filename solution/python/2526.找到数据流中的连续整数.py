"""2526. 找到数据流中的连续整数"""


class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:
        self.streak = self.streak + 1 if num == self.value else 0
        return self.streak >= self.k


if __name__ == "__main__":
    test_cases = [((), None)]
    for _, (args, expected) in enumerate(test_cases):
        stream = DataStream(4, 3)
        assert not stream.consec(4)
        assert not stream.consec(4)
        assert stream.consec(4)
