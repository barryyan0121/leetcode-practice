"""3975. 筛选忙碌区间"""


class Solution:
    def filterOccupiedIntervals(
        self, occupiedIntervals: list[list[int]], freeStart: int, freeEnd: int
    ) -> list[list[int]]:
        occupiedIntervals.sort()
        merged = []
        for start, end in occupiedIntervals:
            if merged and start <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        answer = []
        for start, end in merged:
            if start < freeStart:
                answer.append([start, min(end, freeStart - 1)])
            if end > freeEnd:
                answer.append([max(start, freeEnd + 1), end])
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            ([[2, 6], [4, 8], [10, 10], [10, 12], [14, 16]], 7, 11),
            [[2, 6], [12, 12], [14, 16]],
        ),
        (([[1, 5], [2, 3]], 3, 8), [[1, 2]]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().filterOccupiedIntervals(*args) == expected
