"""3986. Number of Elapsed Seconds Between Two Times"""


class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def to_seconds(time: str) -> int:
            return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:])

        return to_seconds(endTime) - to_seconds(startTime)


if __name__ == "__main__":
    test_cases = [
        (("01:00:00", "01:00:25"), 25),
        (("12:34:56", "13:00:00"), 1504),
        (("00:00:00", "00:00:00"), 0),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().secondsBetweenTimes(*args) == expected
