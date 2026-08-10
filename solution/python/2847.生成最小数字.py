"""2847. 生成最小数字"""


class Solution:
    def smallestNumber(self, n: int) -> str:
        if n == 1:
            return "1"
        digits = []
        for divisor in range(9, 1, -1):
            while n % divisor == 0:
                digits.append(str(divisor))
                n //= divisor
        return "" if n > 1 else "".join(reversed(digits))


if __name__ == "__main__":
    assert Solution().smallestNumber(12) == "26"
