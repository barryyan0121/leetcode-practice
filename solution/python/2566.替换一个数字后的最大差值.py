"""2566. 替换一个数字后的最大差值"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = str(num)
        high_digit = next((digit for digit in digits if digit != "9"), None)
        low_digit = next((digit for digit in digits if digit != "0"), None)
        high = int(digits.replace(high_digit, "9")) if high_digit else num
        low = int(digits.replace(low_digit, "0")) if low_digit else num
        return high - low


if __name__ == "__main__":
    assert Solution().minMaxDifference(11891) == 99009
