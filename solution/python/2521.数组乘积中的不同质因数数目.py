"""2521. 数组乘积中的不同质因数数目"""


class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        factors = set()
        for value in nums:
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    factors.add(divisor)
                    while value % divisor == 0:
                        value //= divisor
                divisor += 1
            if value > 1:
                factors.add(value)
        return len(factors)


if __name__ == "__main__":
    test_cases = [(([2, 4, 3, 7, 10, 6],), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().distinctPrimeFactors(*args) == expected
