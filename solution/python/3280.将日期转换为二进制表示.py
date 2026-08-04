class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split("-")
        return "-".join(format(int(value), "b") for value in (year, month, day))


if __name__ == "__main__":
    test_cases = [
        ("2080-02-29", "100000100000-10-11101"),
        ("1900-01-01", "11101101100-1-1"),
    ]
    for _, (date, expected) in enumerate(test_cases):
        assert Solution().convertDateToBinary(date) == expected
