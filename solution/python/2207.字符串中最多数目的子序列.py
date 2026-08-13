"""2207. 字符串中最多数目的子序列"""


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        if pattern[0] == pattern[1]:
            count = text.count(pattern[0])
            return count * (count + 1) // 2
        left = text.count(pattern[0])
        right = text.count(pattern[1])
        base = 0
        suffix = 0
        for char in reversed(text):
            if char == pattern[1]:
                suffix += 1
            if char == pattern[0]:
                base += suffix
        return base + max(left, right)


if __name__ == "__main__":
    assert Solution().maximumSubsequenceCount("abdcdbc", "ac") == 4
