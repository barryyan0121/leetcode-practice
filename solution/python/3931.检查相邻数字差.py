"""3931. 检查相邻数字差"""


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return all(abs(int(left) - int(right)) <= 2 for left, right in zip(s, s[1:]))


if __name__ == "__main__":
    test_cases = [("132", True), ("129", False)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().isAdjacentDiffAtMostTwo(s) == expected
