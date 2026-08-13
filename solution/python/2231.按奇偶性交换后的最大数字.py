"""2231. 按奇偶性交换后的最大数字"""


class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))
        odds = sorted((d for d in digits if int(d) % 2), reverse=True)
        evens = sorted((d for d in digits if int(d) % 2 == 0), reverse=True)
        oi = ei = 0
        for i, digit in enumerate(digits):
            if int(digit) % 2:
                digits[i] = odds[oi]
                oi += 1
            else:
                digits[i] = evens[ei]
                ei += 1
        return int("".join(digits))


if __name__ == "__main__":
    assert Solution().largestInteger(1234) == 3412
