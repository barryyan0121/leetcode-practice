"""2496. 数组中字符串的最大值"""


class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        return max(int(value) if value.isdigit() else len(value) for value in strs)


if __name__ == "__main__":
    assert Solution().maximumValue(["alic3", "bob", "3", "4", "00000"]) == 5
