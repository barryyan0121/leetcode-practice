class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        dp = {}
        for word in sorted(words, key=len):
            dp[word] = 1 + max(
                (dp.get(word[:i] + word[i + 1 :], 0) for i in range(len(word))),
                default=0,
            )
        return max(dp.values())


if __name__ == "__main__":
    test_cases = [
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
    ]
    for _, (words, expected) in enumerate(test_cases):
        assert Solution().longestStrChain(words) == expected
