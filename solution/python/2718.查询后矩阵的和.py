class Solution:
    def matrixSumQueries(self, n: int, queries: list[list[int]]) -> int:
        rows, cols = set(), set()
        ans = 0
        for typ, idx, val in reversed(queries):
            if typ == 0 and idx not in rows:
                rows.add(idx)
                ans += val * (n - len(cols))
            elif typ == 1 and idx not in cols:
                cols.add(idx)
                ans += val * (n - len(rows))
        return ans


if __name__ == "__main__":
    assert (
        Solution().matrixSumQueries(3, [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]])
        == 23
    )
