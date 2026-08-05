"""2417. 最近的公平整数"""

from functools import lru_cache


class Solution:
    def closestFair(self, n: int) -> int:
        def build(length: int, lower: str | None) -> int | None:
            target = length // 2

            @lru_cache(None)
            def dfs(pos: int, even: int, greater: bool) -> str | None:
                if pos == length:
                    return "" if even == target else None
                start = 1 if pos == 0 else 0
                if lower is not None and not greater:
                    start = max(start, int(lower[pos]))
                for digit in range(start, 10):
                    next_even = even + (digit % 2 == 0)
                    if next_even > target or next_even + length - pos - 1 < target:
                        continue
                    suffix = dfs(
                        pos + 1,
                        next_even,
                        greater or lower is None or digit > int(lower[pos]),
                    )
                    if suffix is not None:
                        return str(digit) + suffix
                return None

            result = dfs(0, 0, False)
            return int(result) if result is not None else None

        length = len(str(n))
        if length % 2:
            length += 1
        return build(length, str(n) if length == len(str(n)) else None) or build(
            length + 2, None
        )


if __name__ == "__main__":
    test_cases = [((1,), 10)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().closestFair(*args) == expected
