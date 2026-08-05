"""2601. 质数减法运算"""


class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        primes = []
        for number in range(2, 1001):
            if all(number % factor for factor in range(2, int(number**0.5) + 1)):
                primes.append(number)
        previous = 0
        for number in nums:
            candidates = [
                prime
                for prime in primes
                if prime < number and number - prime > previous
            ]
            current = number - max(candidates, default=0)
            if current <= previous:
                return False
            previous = current
        return True


if __name__ == "__main__":
    test_cases = [(([4, 9, 6, 10],), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().primeSubOperation(*args) == expected
