"""3556. 最大质数子字符串之和"""


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        primes = set()
        for left in range(len(s)):
            value = 0
            for right in range(left, len(s)):
                value = value * 10 + int(s[right])
                if value > 1 and all(
                    value % divisor for divisor in range(2, int(value**0.5) + 1)
                ):
                    primes.add(value)
        return sum(sorted(primes, reverse=True)[:3])


if __name__ == "__main__":
    test_cases = [
        (("12234",), 1469),
        (("111",), 11),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().sumOfLargestPrimes(s) == expected
