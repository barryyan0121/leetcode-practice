"""3125. 最大与值为零的最大数字"""


class Solution:
    def maxNumber(self, n: int) -> int:
        return (1 << (n.bit_length() - 1)) - 1


if __name__ == "__main__":
    assert Solution().maxNumber(5) == 3
