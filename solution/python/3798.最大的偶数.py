class Solution:
    def largestEven(self, s: str) -> str:
        last_two = s.rfind("2")
        return s[: last_two + 1] if last_two >= 0 else ""


if __name__ == "__main__":
    s = Solution()
    assert s.largestEven("1112") == "1112"
    assert s.largestEven("221") == "22"
    assert s.largestEven("1") == ""
