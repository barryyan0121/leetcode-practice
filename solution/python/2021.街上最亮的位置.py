"""2021. 街上最亮的位置"""

from collections import defaultdict


class Solution:
    def brightestPosition(self, lights: list[list[int]]) -> int:
        events = defaultdict(int)
        for position, radius in lights:
            events[position - radius] += 1
            events[position + radius + 1] -= 1
        current = answer = 0
        best = -1
        for position in sorted(events):
            current += events[position]
            if current > best:
                best, answer = current, position
        return answer


if __name__ == "__main__":
    test_cases = [(([[2, 1], [0, 1]],), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().brightestPosition(*args) == expected
