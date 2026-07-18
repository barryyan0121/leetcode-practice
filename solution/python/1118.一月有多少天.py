class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if month == 2:
            return 29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28
        return 30 if month in (4, 6, 9, 11) else 31


if __name__ == "__main__":
    test_cases = [(1992, 7, 31), (2000, 2, 29), (1900, 2, 28), (2020, 2, 29)]
    for _, (year, month, expected) in enumerate(test_cases):
        assert Solution().numberOfDays(year, month) == expected
