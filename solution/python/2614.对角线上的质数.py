"""2614. 对角线上的质数"""


class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        def is_prime(number):
            return number > 1 and all(
                number % factor for factor in range(2, int(number**0.5) + 1)
            )

        candidates = []
        for index in range(len(nums)):
            candidates.extend((nums[index][index], nums[index][-index - 1]))
        return max((number for number in candidates if is_prime(number)), default=0)


if __name__ == "__main__":
    test_cases = [(([[1, 2, 3], [5, 6, 7], [9, 10, 11]],), 11)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().diagonalPrime(*args) == expected
