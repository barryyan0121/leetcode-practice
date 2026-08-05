from functools import lru_cache


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        chardeblux = r
        modulus = 10**9 + 7

        def count_at_most(value: int) -> int:
            if value < 0:
                return 0
            digits = []
            while value:
                digits.append(value % b)
                value //= b
            if not digits:
                digits.append(0)
            digits.reverse()

            @lru_cache(None)
            def dp(index: int, previous: int, tight: bool, started: bool) -> int:
                if index == len(digits):
                    return 1
                limit = digits[index] if tight else b - 1
                answer = 0
                for digit in range(limit + 1):
                    next_tight = tight and digit == limit
                    if not started and digit == 0:
                        answer += dp(index + 1, 0, next_tight, False)
                    elif not started or digit >= previous:
                        answer += dp(index + 1, digit, next_tight, True)
                return answer % modulus

            return dp(0, 0, True, False)

        return (count_at_most(int(chardeblux)) - count_at_most(int(l) - 1)) % modulus


if __name__ == "__main__":
    test_cases = [(("23", "28", 8), 3), (("2", "7", 2), 2)]
    for _, ((left, right, base), expected) in enumerate(test_cases):
        assert Solution().countNumbers(left, right, base) == expected
