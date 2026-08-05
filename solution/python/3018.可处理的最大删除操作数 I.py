"""3018. 可处理的最大删除操作数 I"""


class Solution:
    def maximumProcessableQueries(self, nums: list[int], queries: list[int]) -> int:
        n, m = len(nums), len(queries)
        dp = [[0] * n for _ in range(n)]
        answer = 0

        def can(value: int, processed: int) -> int:
            return int(processed < m and value >= queries[processed])

        for left in range(n):
            for right in range(n - 1, left - 1, -1):
                if left:
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left - 1][right] + can(nums[left - 1], dp[left - 1][right]),
                    )
                if right < n - 1:
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][right + 1] + can(nums[right + 1], dp[left][right + 1]),
                    )
                answer = max(answer, dp[left][right] + can(nums[left], dp[left][right]))
                if answer == m:
                    return m
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumProcessableQueries(*args) == expected
