"""2054. 两个最好的不重叠活动"""

from bisect import bisect_right


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort()
        starts = []
        for start, _, _ in events:
            starts.append(start)
        suffix = [0] * (len(events) + 1)
        for index in range(len(events) - 1, -1, -1):
            suffix[index] = max(suffix[index + 1], events[index][2])
        answer = 0
        for _, end, value in events:
            index = bisect_right(starts, end)
            answer = max(answer, value + suffix[index])
        return answer


if __name__ == "__main__":
    test_cases = [(([[1, 3, 2], [4, 5, 2], [2, 4, 3]],), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxTwoEvents(*args) == expected
