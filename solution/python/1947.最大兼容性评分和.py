"""1947. 最大兼容性评分和"""


class Solution:
    def maxCompatibilitySum(
        self, students: list[list[int]], mentors: list[list[int]]
    ) -> int:
        n = len(students)
        score = [
            [sum(a == b for a, b in zip(students[i], mentors[j])) for j in range(n)]
            for i in range(n)
        ]
        dp = {0: 0}
        for i in range(n):
            next_dp = {}
            for mask, value in dp.items():
                for j in range(n):
                    if not mask >> j & 1:
                        new_mask = mask | 1 << j
                        next_dp[new_mask] = max(
                            next_dp.get(new_mask, 0), value + score[i][j]
                        )
            dp = next_dp
        return dp[(1 << n) - 1]


if __name__ == "__main__":
    test_cases = [(([[1, 1, 0], [1, 0, 1]], [[1, 0, 0], [0, 0, 1]]), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxCompatibilitySum(*args) == expected
