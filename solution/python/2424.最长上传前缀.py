"""2424. 最长上传前缀"""


class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = [False] * (n + 1)
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.prefix + 1 < len(self.uploaded) and self.uploaded[self.prefix + 1]:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix


if __name__ == "__main__":
    test_cases = [(4, 0)]
    for _, (size, expected) in enumerate(test_cases):
        assert LUPrefix(size).longest() == expected
