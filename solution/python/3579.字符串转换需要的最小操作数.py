"""3579. 字符串转换需要的最小操作数"""


class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        costs = [[0] * n for _ in range(n)]

        def segment_cost(left, right, reverse):
            counts = [[0] * 26 for _ in range(26)]
            different = 0
            for index in range(left, right + 1):
                source = word1[left + right - index] if reverse else word1[index]
                target = word2[index]
                if source != target:
                    different += 1
                    counts[ord(source) - 97][ord(target) - 97] += 1
            swaps = sum(
                min(counts[first][second], counts[second][first])
                for first in range(26)
                for second in range(first + 1, 26)
            )
            return different - swaps + reverse

        for left in range(n):
            for right in range(left, n):
                costs[left][right] = min(
                    segment_cost(left, right, False),
                    segment_cost(left, right, True),
                )

        dp = [10**9] * (n + 1)
        dp[0] = 0
        for end in range(1, n + 1):
            dp[end] = min(
                dp[end], min(dp[start] + costs[start][end - 1] for start in range(end))
            )
        return dp[n]


if __name__ == "__main__":
    test_cases = [
        (("abcdf", "dacbe"), 4),
        (("abceded", "baecfef"), 4),
        (("abcdef", "fedabc"), 2),
    ]
    for _, ((word1, word2), expected) in enumerate(test_cases):
        assert Solution().minOperations(word1, word2) == expected
