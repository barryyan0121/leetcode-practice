"""3581. 计算数字中的奇数字母数量"""

from collections import Counter


class Solution:
    def countOddLetters(self, n: int) -> int:
        words = (
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        )
        counts = Counter("".join(words[int(digit)] for digit in str(n)))
        return sum(count % 2 for count in counts.values())


if __name__ == "__main__":
    test_cases = [((41,), 5), ((20,), 5)]
    for _, ((n,), expected) in enumerate(test_cases):
        assert Solution().countOddLetters(n) == expected
