"""2546. 执行逐位运算使字符串相等"""


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ("1" in s) == ("1" in target)


if __name__ == "__main__":
    test_cases = [(("1010", "0110"), True), (("11", "00"), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().makeStringsEqual(*args) == expected
