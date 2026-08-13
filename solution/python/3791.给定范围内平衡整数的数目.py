from functools import lru_cache


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def count(x: int) -> int:
            if x <= 0:
                return 0
            digits = list(map(int, str(x)))

            @lru_cache(None)
            def dp(pos, tight, started, parity, diff, length):
                if pos == len(digits):
                    return int(started and length == 2 and diff == 0)
                limit = digits[pos] if tight else 9
                answer = 0
                for digit in range(limit + 1):
                    next_tight = tight and digit == digits[pos]
                    if not started and digit == 0:
                        answer += dp(pos + 1, next_tight, False, 0, 0, 0)
                    else:
                        next_diff = diff + (digit if parity == 0 else -digit)
                        next_length = min(2, length + 1)
                        answer += dp(
                            pos + 1,
                            next_tight,
                            True,
                            parity ^ 1,
                            next_diff,
                            next_length,
                        )
                return answer

            return dp(0, True, False, 0, 0, 0)

        return count(high) - count(low - 1)


if __name__ == "__main__":
    s = Solution()
    assert s.countBalanced(1, 100) == 9
    assert s.countBalanced(120, 129) == 1
    assert s.countBalanced(1234, 1234) == 0
