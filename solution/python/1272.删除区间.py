from typing import List


class Solution:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        result = []
        start, end = toBeRemoved
        for left, right in intervals:
            if right <= start or left >= end:
                result.append([left, right])
            else:
                if left < start:
                    result.append([left, start])
                if right > end:
                    result.append([end, right])
        return result


if __name__ == "__main__":
    test_cases = [([[0, 2], [3, 4], [5, 7]], [1, 6], [[0, 1], [6, 7]])]
    for _, (intervals, removed, expected) in enumerate(test_cases):
        assert Solution().removeInterval(intervals, removed) == expected
