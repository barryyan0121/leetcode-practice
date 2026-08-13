"""3851. 不违反限制的最大请求数"""

from collections import defaultdict, deque


class Solution:
    def maxRequests(self, requests: list[list[int]], k: int, window: int) -> int:
        groups: dict[int, list[int]] = defaultdict(list)
        for user, time in requests:
            groups[user].append(time)

        kept = 0
        for times in groups.values():
            times.sort()
            active: deque[int] = deque()
            for time in times:
                while active and time - active[0] > window:
                    active.popleft()
                if len(active) < k:
                    active.append(time)
                    kept += 1
        return kept


if __name__ == "__main__":
    test_cases = [
        (([[1, 1], [2, 1], [1, 7], [2, 8]], 1, 4), 4),
        (([[1, 2], [1, 5], [1, 2], [1, 6]], 2, 5), 2),
        (([[1, 1], [2, 5], [1, 2], [3, 9]], 1, 1), 3),
    ]
    for args, expected in test_cases:
        assert Solution().maxRequests(*args) == expected
