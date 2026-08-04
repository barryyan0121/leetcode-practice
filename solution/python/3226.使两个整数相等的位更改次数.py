class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n & k != k:
            return -1
        return (n ^ k).bit_count()


if __name__ == "__main__":
    test_cases = [((13, 4), 2), ((21, 21), 0), ((14, 13), -1)]
    for _, ((n, k), expected) in enumerate(test_cases):
        assert Solution().minChanges(n, k) == expected
