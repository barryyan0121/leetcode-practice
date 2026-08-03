class Solution:
    def findLatestTime(self, s: str) -> str:
        result = list(s)
        if result[0] == "?":
            result[0] = "1" if result[1] in "01?" else "0"
        if result[1] == "?":
            result[1] = "1" if result[0] == "1" else "9"
        if result[3] == "?":
            result[3] = "5"
        if result[4] == "?":
            result[4] = "9"
        return "".join(result)


if __name__ == "__main__":
    test_cases = [("1?:?4", "11:54"), ("0?:5?", "09:59"), ("??:??", "11:59")]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().findLatestTime(s) == expected
