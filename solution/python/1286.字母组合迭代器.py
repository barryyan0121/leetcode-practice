from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = [
            "".join(item) for item in combinations(characters, combinationLength)
        ]
        self.index = 0

    def next(self) -> str:
        result = self.combinations[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)


if __name__ == "__main__":
    test_cases = [("abc", 2, ["ab", "ac", "bc"])]
    for _, (characters, length, expected) in enumerate(test_cases):
        iterator = CombinationIterator(characters, length)
        assert [iterator.next() for _ in expected] == expected
        assert not iterator.hasNext()
