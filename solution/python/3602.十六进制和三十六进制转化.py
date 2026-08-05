"""3602. 十六进制和三十六进制转化"""


class Solution:
    def concatHex36(self, n: int) -> str:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def convert(value: int, base: int) -> str:
            result = ""
            while value:
                result = digits[value % base] + result
                value //= base
            return result or "0"

        return convert(n * n, 16) + convert(n * n * n, 36)


if __name__ == "__main__":
    test_cases = [(13, "A91P1"), (36, "5101000")]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().concatHex36(n) == expected
