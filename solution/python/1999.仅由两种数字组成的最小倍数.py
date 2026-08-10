"""1999. 仅由两种数字组成的最小倍数"""

from collections import deque


class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        if digit1 == 0 and digit2 == 0:
            return -1
        digits = sorted({digit for digit in (digit1, digit2) if digit})
        queue = deque(digits)
        while queue:
            value = queue.popleft()
            if value > 2**31 - 1:
                return -1
            if value > k and value % k == 0:
                return value
            for digit in sorted({digit1, digit2}):
                queue.append(value * 10 + digit)
        return -1


if __name__ == "__main__":
    assert Solution().findInteger(2, 0, 2) == 20
    assert Solution().findInteger(3, 4, 2) == 24
