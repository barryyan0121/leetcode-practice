"""2140. 解决智力问题"""


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        dp = [0] * (len(questions) + 1)
        for index in range(len(questions) - 1, -1, -1):
            points, brainpower = questions[index]
            dp[index] = max(
                dp[index + 1], points + dp[min(len(questions), index + brainpower + 1)]
            )
        return dp[0]


if __name__ == "__main__":
    test_cases = [(([[3, 2], [4, 3], [4, 4], [2, 5]],), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().mostPoints(*args) == expected
