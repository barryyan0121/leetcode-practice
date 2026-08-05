"""2827. 范围中美丽整数的数目"""


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count(bound: int) -> int:
            if bound <= 0:
                return 0
            digits = list(map(int, str(bound)))
            memo = {}

            def dfs(pos, remainder, difference, started, tight):
                if pos == len(digits):
                    return int(started and remainder == 0 and difference == 0)
                key = (pos, remainder, difference, started)
                if not tight and key in memo:
                    return memo[key]
                total = 0
                for digit in range(digits[pos] + 1 if tight else 10):
                    next_started = started or digit != 0
                    if not next_started:
                        total += dfs(
                            pos + 1, 0, 0, False, tight and digit == digits[pos]
                        )
                    else:
                        total += dfs(
                            pos + 1,
                            (remainder * 10 + digit) % k,
                            difference + (1 if digit % 2 else -1),
                            True,
                            tight and digit == digits[pos],
                        )
                if not tight:
                    memo[key] = total
                return total

            return dfs(0, 0, 0, False, True)

        return count(high) - count(low - 1)


if __name__ == "__main__":
    test_cases = [((10, 20, 3), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfBeautifulIntegers(*args) == expected
