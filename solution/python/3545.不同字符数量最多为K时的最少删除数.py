"""3545. 不同字符数量最多为 K 时的最少删除数"""


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        frequencies = sorted(s.count(char) for char in set(s))
        return sum(frequencies[: max(0, len(frequencies) - k)])


if __name__ == "__main__":
    test_cases = [
        (("aabbcc", 2), 2),
        (("aab", 3), 0),
        (("aabb", 0), 4),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().minDeletion(s, k) == expected
