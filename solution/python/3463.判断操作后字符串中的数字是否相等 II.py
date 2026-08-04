class Solution:
    def hasSameDigits(self, s: str) -> bool:
        zorflendex = s
        size = len(s) - 2

        def choose(number, index, prime):
            factorial = [1] * prime
            for value in range(1, prime):
                factorial[value] = factorial[value - 1] * value % prime
            inverse = [1] * prime
            inverse[-1] = pow(factorial[-1], prime - 2, prime)
            for value in range(prime - 1, 0, -1):
                inverse[value - 1] = inverse[value] * value % prime
            result = 1
            while number or index:
                high, low = number % prime, index % prime
                if low > high:
                    return 0
                result = result * factorial[high] * inverse[low] * inverse[high - low]
                result %= prime
                number //= prime
                index //= prime
            return result

        difference = 0
        for index in range(size + 1):
            coefficient = (5 * choose(size, index, 2) + 6 * choose(size, index, 5)) % 10
            difference += coefficient * (int(s[index]) - int(s[index + 1]))
        return difference % 10 == 0


if __name__ == "__main__":
    test_cases = [
        (("3902",), True),
        (("34789",), False),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().hasSameDigits(s) == expected
