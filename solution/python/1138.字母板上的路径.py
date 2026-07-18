class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        row = column = 0
        path = []
        for char in target:
            next_row, next_column = divmod(ord(char) - ord("a"), 5)
            path.extend("U" * (row - next_row))
            path.extend("L" * (column - next_column))
            path.extend("D" * (next_row - row))
            path.extend("R" * (next_column - column))
            path.append("!")
            row, column = next_row, next_column
        return "".join(path)


if __name__ == "__main__":
    test_cases = [
        ("leet", "DDR!UURRR!!DDD!"),
        ("code", "RR!DDRR!UUL!R!"),
        ("zdz", "DDDDD!UUUUURRR!LLLDDDDD!"),
    ]
    for _, (target, expected) in enumerate(test_cases):
        assert Solution().alphabetBoardPath(target) == expected
