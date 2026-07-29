from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        return min(
            counts["b"], counts["a"], counts["l"] // 2, counts["o"] // 2, counts["n"]
        )


if __name__ == "__main__":
    test_cases = [("nlaebolko", 1), ("loonbalxballpoon", 2), ("leetcode", 0)]
    for _, (text, expected) in enumerate(test_cases):
        assert Solution().maxNumberOfBalloons(text) == expected
