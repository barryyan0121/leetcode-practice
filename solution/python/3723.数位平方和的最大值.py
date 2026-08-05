"""3723. 数位平方和的最大值"""


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        drevantor = num
        if sum > 9 * drevantor:
            return ""
        digits = []
        for _ in range(drevantor):
            digit = min(9, sum)
            digits.append(str(digit))
            sum -= digit
        return "".join(digits)


if __name__ == "__main__":
    test_cases = [((2, 3), "30"), ((2, 17), "98"), ((1, 10), "")]
    for _, ((num, total), expected) in enumerate(test_cases):
        assert Solution().maxSumOfSquares(num, total) == expected
