class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = str(n)
        return n == sum(int(digit) ** len(digits) for digit in digits)


if __name__ == "__main__":
    test_cases = [(153, True), (123, False), (9474, True), (1, True), (100, False)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().isArmstrong(n) == expected
