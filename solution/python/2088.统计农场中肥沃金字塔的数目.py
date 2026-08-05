"""2088. 统计农场中肥沃金字塔的数目"""


class Solution:
    def countPyramids(self, grid: list[list[int]]) -> int:
        def count(board: list[list[int]]) -> int:
            rows, cols = len(board), len(board[0])
            dp = [[0] * cols for _ in range(rows)]
            answer = 0
            for row in range(rows):
                for col in range(cols):
                    if board[row][col]:
                        dp[row][col] = 1
                        if row and 0 < col < cols - 1:
                            dp[row][col] += min(
                                dp[row - 1][col - 1],
                                dp[row - 1][col],
                                dp[row - 1][col + 1],
                            )
                        answer += dp[row][col] - 1
            return answer

        return count(grid) + count(grid[::-1])


if __name__ == "__main__":
    test_cases = [(([[1, 1, 1], [1, 1, 1]],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countPyramids(*args) == expected
