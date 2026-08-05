"""1999. 最小的仅由两个数组成的倍数"""

from collections import deque


class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        digits = sorted({digit1, digit2})
        queue = deque()
        seen = set()
        for digit in digits:
            if digit and digit % k not in seen:
                seen.add(digit % k)
                queue.append((digit % k, digit))
        while queue:
            remainder, value = queue.popleft()
            if remainder == 0:
                return value
            for digit in digits:
                next_remainder = (remainder * 10 + digit) % k
                if next_remainder not in seen:
                    seen.add(next_remainder)
                    queue.append((next_remainder, value * 10 + digit))
        return -1


if __name__ == "__main__":
    test_cases = [((3, 4, 5), 45)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findInteger(*args) == expected
