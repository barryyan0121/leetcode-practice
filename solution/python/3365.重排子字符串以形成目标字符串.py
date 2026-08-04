from collections import Counter


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        block_length = len(s) // k
        source = Counter(
            s[index : index + block_length] for index in range(0, len(s), block_length)
        )
        target = Counter(
            t[index : index + block_length] for index in range(0, len(t), block_length)
        )
        return source == target


if __name__ == "__main__":
    test_cases = [
        (("abcd", "cdab", 2), True),
        (("aabb", "abab", 2), False),
        (("abc", "abc", 1), True),
    ]
    for _, ((s, t, k), expected) in enumerate(test_cases):
        assert Solution().isPossibleToRearrange(s, t, k) == expected
