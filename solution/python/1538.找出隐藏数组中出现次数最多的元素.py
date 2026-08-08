class ArrayReader:
    def __init__(self, values: list[int]):
        self.values = values

    def query(self, a: int, b: int, c: int, d: int) -> int:
        ones = sum(self.values[index] for index in (a, b, c, d))
        return 4 if ones in (0, 4) else 2 if ones in (1, 3) else 0

    def length(self) -> int:
        return len(self.values)


class Solution:
    def guessMajority(self, reader: "ArrayReader") -> int:
        base = reader.query(0, 1, 2, 3)
        reference = reader.query(1, 2, 3, 4)
        count, answer = (2, 4) if base == reference else (0, 4)
        for index, query in enumerate(
            (
                reader.query(0, 2, 3, 4),
                reader.query(0, 1, 3, 4),
                reader.query(0, 1, 2, 4),
            ),
            1,
        ):
            if query == reference:
                count += 1
            else:
                count -= 1
                answer = index
        for index in range(5, reader.length()):
            if reader.query(1, 2, 3, index) == base:
                count += 1
            else:
                count -= 1
                answer = index
        return 0 if count > 0 else answer if count < 0 else -1


if __name__ == "__main__":
    test_cases = [
        ([0, 0, 1, 0, 1, 1, 1, 1], {2, 4, 5, 6, 7}),
        ([0, 0, 1, 1, 0], {0, 1, 4}),
        ([1, 0, 1, 0, 1, 0, 1, 0], {-1}),
    ]
    for _, (values, expected) in enumerate(test_cases):
        assert Solution().guessMajority(ArrayReader(values)) in expected
