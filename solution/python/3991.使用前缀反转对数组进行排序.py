"""3991. 使用前缀反转对数组进行排序"""

from collections import deque


class Solution:
    def sortArray(self, nums: list[int], pre: list[int]) -> int:
        start = tuple(nums)
        target = tuple(sorted(nums))
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            for size in pre:
                next_state = state[:size][::-1] + state[size:]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))
        return -1


if __name__ == "__main__":
    test_cases = [
        (([2, 0, 1], [2, 3]), 2),
        (([1, 0, 2], [1, 3]), -1),
        (([0, 1], [2]), 0),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().sortArray(*args) == expected
