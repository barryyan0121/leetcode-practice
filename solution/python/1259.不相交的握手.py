class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        modulo = 10**9 + 7
        dp = [0] * (numPeople + 1)
        dp[0] = 1
        for people in range(2, numPeople + 1, 2):
            dp[people] = (
                sum(dp[left] * dp[people - 2 - left] for left in range(0, people, 2))
                % modulo
            )
        return dp[numPeople]


if __name__ == "__main__":
    test_cases = [(2, 1), (4, 2), (6, 5)]
    for _, (num_people, expected) in enumerate(test_cases):
        assert Solution().numberOfWays(num_people) == expected
