"""604. 迭代压缩字符串"""


class StringIterator:
    def __init__(self, compressedString: str):
        self.parts = []
        index = 0
        while index < len(compressedString):
            char = compressedString[index]
            index += 1
            start = index
            while index < len(compressedString) and compressedString[index].isdigit():
                index += 1
            self.parts.append([char, int(compressedString[start:index])])
        self.index = 0

    def next(self) -> str:
        if not self.hasNext():
            return " "
        char, count = self.parts[self.index]
        self.parts[self.index][1] -= 1
        if self.parts[self.index][1] == 0:
            self.index += 1
        return char

    def hasNext(self) -> bool:
        return self.index < len(self.parts)


if __name__ == "__main__":
    iterator = StringIterator("L1e2t1C1o1d1e1")
    assert [iterator.next() for _ in range(6)] == list("LeetCo")
    assert iterator.hasNext()
