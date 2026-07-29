from datetime import date as CalendarDate


class Solution:
    def dayOfYear(self, date: str) -> int:
        current = date.split("-")
        current = CalendarDate(int(current[0]), int(current[1]), int(current[2]))
        return (current - CalendarDate(current.year, 1, 1)).days + 1


if __name__ == "__main__":
    test_cases = [("2019-01-09", 9), ("2019-02-10", 41), ("2004-03-01", 61)]
    for _, (value, expected) in enumerate(test_cases):
        assert Solution().dayOfYear(value) == expected
