"""3918. 数与其逆序数之间的质数和"""


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        mavroliken = n
        reverse = int(str(mavroliken)[::-1])
        low, high = sorted((mavroliken, reverse))
        total = 0
        for value in range(max(2, low), high + 1):
            if all(value % divisor for divisor in range(2, int(value**0.5) + 1)):
                total += value
        return total


if __name__ == "__main__":
    test_cases = [(13, 132), (10, 17), (8, 0)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().sumOfPrimesInRange(n) == expected
