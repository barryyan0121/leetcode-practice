"""2311. 小于等于 K 的最长二进制子序列"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        length = 0
        value = 0
        power = 1
        for char in reversed(s):
            if char == "0":
                length += 1
            elif value + power <= k:
                value += power
                length += 1
            if power <= k:
                power <<= 1
        return length


if __name__ == "__main__":
    assert Solution().longestSubsequence("1001010", 5) == 5
