class Solution:
    def minConnectedGroups(self, intervals: list[list[int]], k: int) -> int:
        intervals.sort()
        merged = []
        for start, end in intervals:
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        best = 0
        right = 0
        for left, (_, end) in enumerate(merged):
            right = max(right, left)
            while right + 1 < len(merged) and merged[right + 1][0] - end <= k:
                right += 1
            best = max(best, right - left)
        return len(merged) - best


if __name__ == "__main__":
    test_cases = [
        (([[1, 3], [5, 6], [8, 10]], 3), 2),
        (([[5, 10], [1, 1], [3, 3]], 1), 3),
    ]
    for _, ((intervals, k), expected) in enumerate(test_cases):
        assert Solution().minConnectedGroups(intervals, k) == expected
