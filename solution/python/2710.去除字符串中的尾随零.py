"""2710. 去除字符串中的尾随零"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")


if __name__ == "__main__":
    assert Solution().removeTrailingZeros("51230100") == "512301"
