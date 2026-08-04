from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        ordered = sorted(
            (right, left, weight, index)
            for index, (left, right, weight) in enumerate(intervals)
        )
        ends = [item[0] for item in ordered]
        size = len(ordered)
        prefix = [[None] * (size + 1) for _ in range(5)]
        for i in range(size + 1):
            prefix[0][i] = (0, ())

        for i, (right, left, weight, index) in enumerate(ordered, 1):
            previous = bisect_left(ends, left)
            for count in range(1, 5):
                current = prefix[count][i - 1]
                prior = prefix[count - 1][previous]
                if prior is not None:
                    indices = tuple(sorted(prior[1] + (index,)))
                    candidate = (prior[0] + weight, indices)
                    if (
                        current is None
                        or candidate[0] > current[0]
                        or (candidate[0] == current[0] and candidate[1] < current[1])
                    ):
                        current = candidate
                prefix[count][i] = current

        answer = (0, ())
        for count in range(1, 5):
            candidate = prefix[count][size]
            if candidate is not None and (
                candidate[0] > answer[0]
                or candidate[0] == answer[0]
                and candidate[1] < answer[1]
            ):
                answer = candidate
        return list(answer[1])


if __name__ == "__main__":
    test_cases = [
        (([[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3]],), [2, 3]),
        (
            (
                [
                    [5, 8, 1],
                    [6, 7, 7],
                    [4, 7, 3],
                    [9, 10, 6],
                    [7, 8, 2],
                    [11, 14, 3],
                    [3, 5, 5],
                ],
            ),
            [1, 3, 5, 6],
        ),
    ]
    for _, ((intervals,), expected) in enumerate(test_cases):
        assert Solution().maximumWeight(intervals) == expected
