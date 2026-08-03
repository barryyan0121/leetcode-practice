class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        busy = 0
        start = end = None
        for meeting_start, meeting_end in meetings:
            if start is None:
                start, end = meeting_start, meeting_end
            elif meeting_start > end + 1:
                busy += end - start + 1
                start, end = meeting_start, meeting_end
            else:
                end = max(end, meeting_end)
        if start is not None:
            busy += end - start + 1
        return days - busy


if __name__ == "__main__":
    test_cases = [(10, [[5, 7], [1, 3]], 4), (5, [[1, 5]], 0)]
    for _, (days, meetings, expected) in enumerate(test_cases):
        assert Solution().countDays(days, meetings) == expected
