"""2515. 到目标字符串的最短距离"""


class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        return min(
            (
                min((index - startIndex) % n, (startIndex - index) % n)
                for index, word in enumerate(words)
                if word == target
            ),
            default=-1,
        )


if __name__ == "__main__":
    test_cases = [((["hello", "i", "am", "leetcode", "hello"], "hello", 1), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().closetTarget(*args) == expected
