class Solution:
    def minMoves(self, rooks: list[list[int]]) -> int:
        rows = sorted(x for x, _ in rooks)
        cols = sorted(y for _, y in rooks)
        return sum(abs(value - i) for i, value in enumerate(rows)) + sum(
            abs(value - i) for i, value in enumerate(cols)
        )


if __name__ == "__main__":
    assert Solution().minMoves([[1, 1], [1, 1]]) == 2
