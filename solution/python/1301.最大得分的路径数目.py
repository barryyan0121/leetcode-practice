# @lc app=leetcode.cn id=1301 lang=python3

from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        rows, cols = len(board), len(board[0])
        mod = 10**9 + 7
        dp = [[None] * cols for _ in range(rows)]
        dp[rows - 1][cols - 1] = (0, 1)
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if board[r][c] == "X" or (r == rows - 1 and c == cols - 1):
                    continue
                candidates = [
                    dp[nr][nc]
                    for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1))
                    if nr < rows and nc < cols and dp[nr][nc]
                ]
                if not candidates:
                    continue
                best = max(score for score, _ in candidates)
                ways = sum(count for score, count in candidates if score == best) % mod
                cell = board[r][c]
                dp[r][c] = (best + (int(cell) if cell not in "SE" else 0), ways)
        return list(dp[0][0]) if dp[0][0] else [0, 0]


if __name__ == "__main__":
    test_cases = [
        (Solution().pathsWithMaxScore, (["E23", "2X2", "12S"],), [7, 1]),
        (Solution().pathsWithMaxScore, (["E12", "1X1", "21S"],), [4, 2]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1301 题 "最大得分的路径数目" 所有测试用例通过')
