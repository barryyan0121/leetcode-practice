"""2745. 构造最长的新字符串"""


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return 4 * min(x, y) + 2 * z + (2 if x != y else 0)


if __name__ == "__main__":
    assert Solution().longestString(2, 5, 1) == 12
