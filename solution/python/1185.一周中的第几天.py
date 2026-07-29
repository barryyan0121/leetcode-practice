from datetime import date


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime("%A")


if __name__ == "__main__":
    test_cases = [(31, 8, 2019, "Saturday"), (18, 7, 1999, "Sunday")]
    for _, (day, month, year, expected) in enumerate(test_cases):
        assert Solution().dayOfTheWeek(day, month, year) == expected
