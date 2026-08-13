"""2267. 检查是否有合法括号字符串路径"""


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == ")" or grid[-1][-1] == "(" or (rows + cols - 1) % 2 == 1:
            return False
        dp = [[set() for _ in range(cols)] for _ in range(rows)]
        dp[0][0].add(1)
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                previous = set()
                if i:
                    previous |= dp[i - 1][j]
                if j:
                    previous |= dp[i][j - 1]
                delta = 1 if grid[i][j] == "(" else -1
                dp[i][j] = {
                    balance + delta for balance in previous if balance + delta >= 0
                }
        return 0 in dp[-1][-1]


if __name__ == "__main__":
    assert not Solution().hasValidPath([["(", "("], [")", ")"]])
