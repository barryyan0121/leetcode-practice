"""2998. 使 X 和 Y 相等的最少操作次数"""

from collections import deque


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y - x
        upper = x + (x - y)
        queue = deque([(x, 0)])
        visited = {x}
        while queue:
            value, distance = queue.popleft()
            if value == y:
                return distance
            for next_value in (value - 1, value + 1):
                if y <= next_value <= upper and next_value not in visited:
                    visited.add(next_value)
                    queue.append((next_value, distance + 1))
            for divisor in (5, 11):
                if value % divisor == 0 and value // divisor not in visited:
                    visited.add(value // divisor)
                    queue.append((value // divisor, distance + 1))
        return upper - y


if __name__ == "__main__":
    test_cases = [((26, 1), 3), ((54, 2), 4), ((25, 30), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumOperationsToMakeEqual(*args) == expected
