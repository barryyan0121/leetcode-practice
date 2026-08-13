from functools import reduce

MOD = 10**9 + 7
LIMIT = 5000


def digit_sum(value: int) -> int:
    total = 0
    while value:
        value, remainder = divmod(value, 10)
        total += remainder
    return total


def build_lookup(limit: int) -> list[list[int]]:
    lookup = [[] for _ in range(limit + 1)]
    for value in range(limit + 1):
        lookup[digit_sum(value)].append(value)
    return lookup


LOOKUP = build_lookup(LIMIT)


class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        dp = [(0, 1)]
        for target in digitSum:
            new_dp = []
            prefix = 0
            index = 0
            for value in LOOKUP[target]:
                while index < len(dp) and dp[index][0] <= value:
                    prefix = (prefix + dp[index][1]) % MOD
                    index += 1
                if prefix:
                    new_dp.append((value, prefix))
            dp = new_dp
        return reduce(lambda acc, item: (acc + item[1]) % MOD, dp, 0)


if __name__ == "__main__":
    test_cases = [
        ([25, 1], 6),
        ([1], 4),
    ]
    for _, (digit_sum_values, expected) in enumerate(test_cases):
        assert Solution().countArrays(digit_sum_values) == expected
