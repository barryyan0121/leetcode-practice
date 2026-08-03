# @lc app=leetcode.cn id=1563 lang=python3


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        from bisect import bisect_left

        n = len(stoneValue)
        prefix = [0]
        for value in stoneValue:
            prefix.append(prefix[-1] + value)
        dp = [[0] * n for _ in range(n)]
        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]
        for index in range(n):
            left_best[index][index] = prefix[index + 1]
            right_best[index][index] = -prefix[index]
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                total = prefix[right + 1] - prefix[left]
                middle = bisect_left(
                    prefix, prefix[left] + total / 2, left + 1, right + 1
                )
                equal = prefix[middle] * 2 == prefix[left] + prefix[right + 1]
                left_end = middle - 1 if equal else middle - 2
                if left_end >= left:
                    dp[left][right] = left_best[left][left_end] - prefix[left]
                if middle - 1 < right:
                    dp[left][right] = max(
                        dp[left][right],
                        prefix[right + 1] + right_best[middle][right],
                    )
                left_best[left][right] = max(
                    left_best[left][right - 1], prefix[right + 1] + dp[left][right]
                )
                right_best[left][right] = max(
                    right_best[left + 1][right], dp[left][right] - prefix[left]
                )
        return dp[0][-1]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.stoneGameV, ([6, 2, 3, 4, 5, 5],), 18),
        (solution.stoneGameV, ([7, 7, 7, 7, 7, 7, 7],), 28),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1563 题 "石子游戏 V" 所有测试用例通过')
