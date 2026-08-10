"""2384. 最大回文数"""


class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = [num.count(str(digit)) for digit in range(10)]
        if not any(counts[digit] // 2 for digit in range(1, 10)):
            counts[0] = 0
        left = []
        for digit in range(9, -1, -1):
            pairs = counts[digit] // 2
            left.append(str(digit) * pairs)
        left = "".join(left)
        middle = next(
            (str(digit) for digit in range(9, -1, -1) if counts[digit] % 2), ""
        )
        if not left and not middle:
            return "0"
        return left + middle + left[::-1]
