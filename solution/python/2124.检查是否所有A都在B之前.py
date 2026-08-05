"""2124. 检查是否所有 A 都在 B 之前"""


class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s


if __name__ == "__main__":
    test_cases = [("aaabbb", True), (("abab",), False)]
    for _, (args, expected) in enumerate(test_cases):
        args = (args,) if isinstance(args, str) else args
        assert Solution().checkString(*args) == expected
