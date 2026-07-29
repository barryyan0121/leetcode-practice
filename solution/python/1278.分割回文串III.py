class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        length = len(s)
        cost = [[0] * length for _ in s]
        for start in range(length - 2, -1, -1):
            for end in range(start + 1, length):
                cost[start][end] = (s[start] != s[end]) + cost[start + 1][end - 1]
        best = [[length] * (length + 1) for _ in range(k + 1)]
        best[0][0] = 0
        for parts in range(1, k + 1):
            for end in range(parts, length + 1):
                best[parts][end] = min(
                    best[parts - 1][start] + cost[start][end - 1]
                    for start in range(parts - 1, end)
                )
        return best[k][length]


if __name__ == "__main__":
    test_cases = [(("abc", 2), 1), (("aabbc", 3), 0), (("leetcode", 8), 0)]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().palindromePartition(s, k) == expected
