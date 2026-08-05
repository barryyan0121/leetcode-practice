"""2018. 判断单词是否能放入填字游戏内"""


class Solution:
    def placeWordInCrossword(self, board: list[list[str]], word: str) -> bool:
        def fits(line: list[str]) -> bool:
            for start in range(len(line) - len(word) + 1):
                end = start + len(word)
                if (start == 0 or line[start - 1] == "#") and (
                    end == len(line) or line[end] == "#"
                ):
                    part = line[start:end]
                    if all(a == " " or a == b for a, b in zip(part, word)) or all(
                        a == " " or a == b for a, b in zip(part, word[::-1])
                    ):
                        return True
            return False

        rows = board + [list(column) for column in zip(*board)]
        return any(fits(line) for row in rows for line in _segments(row))


def _segments(line: list[str]):
    start = 0
    for i in range(len(line) + 1):
        if i == len(line) or line[i] == "#":
            if i > start:
                yield line[start:i]
            start = i + 1


if __name__ == "__main__":
    test_cases = [(([["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "abc"), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().placeWordInCrossword(*args) == expected
