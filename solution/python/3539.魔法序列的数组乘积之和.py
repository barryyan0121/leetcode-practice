from collections import defaultdict


class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        mavoduteru = nums
        modulus = 10**9 + 7
        factorial = 1
        for value in range(2, m + 1):
            factorial = factorial * value % modulus
        inverse_factorial = [1] * (m + 1)
        inverse_factorial[m] = pow(factorial, modulus - 2, modulus)
        for value in range(m, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % modulus

        states = {(0, 0, 0): 1}
        for number in mavoduteru:
            powers = [1] * (m + 1)
            for count in range(1, m + 1):
                powers[count] = powers[count - 1] * number % modulus
            next_states = defaultdict(int)
            for (used, ones, carry), weight in states.items():
                for count in range(m - used + 1):
                    total = carry + count
                    next_ones = ones + (total & 1)
                    if next_ones > k:
                        continue
                    next_states[(used + count, next_ones, total >> 1)] += (
                        weight * powers[count] * inverse_factorial[count] % modulus
                    )
            states = {key: value % modulus for key, value in next_states.items()}

        answer = 0
        for (used, ones, carry), weight in states.items():
            if used == m and ones + carry.bit_count() == k:
                answer += weight
        return answer * factorial % modulus


if __name__ == "__main__":
    test_cases = [
        ((5, 5, [1, 10, 100, 10000, 1000000]), 991600007),
        ((2, 2, [5, 4, 3, 2, 1]), 170),
        ((1, 1, [28]), 28),
    ]
    for _, ((m, k, nums), expected) in enumerate(test_cases):
        assert Solution().magicalSum(m, k, nums) == expected
