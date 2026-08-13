"""2847. 给定数字乘积的最小数字"""


class Solution:
    def smallestNumber(self, n: int) -> str:
        if n < 10:
            return str(n)
        digits = []
        for factor in range(9, 1, -1):
            while n % factor == 0:
                digits.append(str(factor))
                n //= factor
        return "-1" if n != 1 else "".join(sorted(digits))


if __name__ == "__main__":
    assert Solution().smallestNumber(105) == "357"
    assert Solution().smallestNumber(7) == "7"
    assert Solution().smallestNumber(44) == "-1"
