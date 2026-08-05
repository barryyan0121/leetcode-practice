"""2052. 将句子分隔成行的最低成本"""


class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        words = sentence.split()
        count = len(words)
        dp = [float("inf")] * (count + 1)
        dp[0] = 0
        for start in range(count):
            length = 0
            for end in range(start, count):
                length += len(words[end]) + (end > start)
                if length > k:
                    break
                cost = 0 if end == count - 1 else (k - length) ** 2
                dp[end + 1] = min(dp[end + 1], dp[start] + cost)
        return dp[count]


if __name__ == "__main__":
    test_cases = [(("i love leetcode", 12), 36), (("a", 5), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumCost(*args) == expected
