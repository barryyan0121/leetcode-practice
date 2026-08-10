"""2194. Excel 表中某个范围内的单元格"""


class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        return [
            f"{chr(column)}{row}"
            for column in range(ord(s[0]), ord(s[3]) + 1)
            for row in range(int(s[1]), int(s[4]) + 1)
        ]


if __name__ == "__main__":
    assert Solution().cellsInRange("K1:L2") == ["K1", "K2", "L1", "L2"]
