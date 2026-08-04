class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        prefix = []
        for column in range(n):
            sums = [0]
            for row in range(n):
                sums.append(sums[-1] + grid[row][column])
            prefix.append(sums)

        size = n + 1
        negative_infinity = -(10**18)
        dp = [[negative_infinity] * size for _ in range(size)]
        for first in range(size):
            for second in range(size):
                dp[first][second] = prefix[0][max(first, second)] - prefix[0][first]

        for column in range(1, n - 1):
            current_prefix = prefix[column]
            next_dp = [[negative_infinity] * size for _ in range(size)]
            for current_height in range(size):
                best_prefix = [negative_infinity] * size
                best = negative_infinity
                for previous_height in range(size):
                    best = max(best, dp[previous_height][current_height])
                    best_prefix[previous_height] = best

                best_suffix = [negative_infinity] * (size + 1)
                best = negative_infinity
                for previous_height in range(size - 1, -1, -1):
                    best = max(
                        best,
                        dp[previous_height][current_height]
                        + current_prefix[max(current_height, previous_height)],
                    )
                    best_suffix[previous_height] = best

                for next_height in range(size):
                    best = (
                        best_prefix[next_height]
                        + current_prefix[max(current_height, next_height)]
                    )
                    if next_height + 1 < size:
                        best = max(best, best_suffix[next_height + 1])
                    next_dp[current_height][next_height] = (
                        best - current_prefix[current_height]
                    )
            dp = next_dp

        last_prefix = prefix[-1]
        return max(
            dp[previous_height][last_height]
            + last_prefix[max(previous_height, last_height)]
            - last_prefix[last_height]
            for previous_height in range(size)
            for last_height in range(size)
        )


if __name__ == "__main__":
    test_cases = [
        (
            [
                [0, 0, 0, 0, 0],
                [0, 0, 3, 0, 0],
                [0, 1, 0, 0, 0],
                [5, 0, 0, 3, 0],
                [0, 0, 0, 0, 2],
            ],
            11,
        ),
        (
            [
                [10, 9, 0, 0, 15],
                [7, 1, 0, 8, 0],
                [5, 20, 0, 11, 0],
                [0, 0, 0, 1, 2],
                [8, 12, 1, 10, 3],
            ],
            94,
        ),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().maximumScore(grid) == expected
