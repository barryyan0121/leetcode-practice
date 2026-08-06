"""4005. 使数组中所有元素相等的最小操作数 III"""

from collections import Counter
from math import isqrt


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        frequency = Counter(nums)
        if len(frequency) == 1:
            return 0
        limit = isqrt(10**9) + 1
        sieve = bytearray(b"\x01") * (limit + 1)
        sieve[:2] = b"\x00\x00"
        for prime in range(2, isqrt(limit) + 1):
            if sieve[prime]:
                sieve[prime * prime :: prime] = b"\x00" * (
                    (limit - prime * prime) // prime + 1
                )
        primes = [prime for prime, enabled in enumerate(sieve) if enabled]

        divisor_cache = {}

        def divisors(value: int) -> list[int]:
            if value in divisor_cache:
                return divisor_cache[value]
            original = value
            answer = [1]
            for prime in primes:
                if prime * prime > value:
                    break
                if value % prime:
                    continue
                power = 1
                factors = []
                while value % prime == 0:
                    value //= prime
                    power *= prime
                    factors.append(power)
                answer += [
                    divisor * factor for divisor in answer[:] for factor in factors
                ]
            if value > 1:
                answer += [divisor * value for divisor in answer]
            divisor_cache[original] = answer
            return answer

        divisible_by = Counter()
        for value, amount in frequency.items():
            for divisor in divisors(value):
                divisible_by[divisor] += amount

        answer = len(nums)
        for target in frequency:
            if target == 1:
                continue
            divisor_count = sum(
                frequency.get(divisor, 0) for divisor in divisors(target)
            )
            answer = min(answer, 2 * len(nums) - divisible_by[target] - divisor_count)
        return answer


if __name__ == "__main__":
    test_cases = [(([6, 12, 8],), 3), (([5, 15, 20],), 2), (([7, 7, 7],), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
