"""1941. 检查是否所有字符出现次数相同"""

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1


if __name__ == "__main__":
    test_cases = [(("abacbc",), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().areOccurrencesEqual(*args) == expected
