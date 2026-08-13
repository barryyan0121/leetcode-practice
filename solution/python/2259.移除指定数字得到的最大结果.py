"""2259. 移除指定数字得到的最大结果"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i in range(len(number) - 1):
            if number[i] == digit and number[i + 1] > digit:
                return number[:i] + number[i + 1 :]
        i = number.rfind(digit)
        return number[:i] + number[i + 1 :]

if __name__ == "__main__":
    assert Solution().removeDigit("1231", "1") == "231"
