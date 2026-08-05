"""2664. 巡逻的骑士"""


class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> list[list[int]]:
        moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        board = [[-1] * n for _ in range(m)]
        board[r][c] = 0

        def dfs(i: int, j: int, step: int) -> bool:
            if step == m * n:
                return True
            candidates = []
            for di, dj in moves:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] < 0:
                    degree = sum(
                        0 <= ni + ddi < m
                        and 0 <= nj + ddj < n
                        and board[ni + ddi][nj + ddj] < 0
                        for ddi, ddj in moves
                    )
                    candidates.append((degree, ni, nj))
            for _, ni, nj in sorted(candidates):
                board[ni][nj] = step
                if dfs(ni, nj, step + 1):
                    return True
                board[ni][nj] = -1
            return False

        dfs(r, c, 1)
        return board


if __name__ == "__main__":
    test_cases = [((1, 1, 0, 0), [[0]])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().tourOfKnight(*args) == expected
