"""2220. 转换数字的最少位翻转次数"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
