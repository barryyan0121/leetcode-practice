class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        last_seen = {}
        start = -1
        count = 0
        for index, char in enumerate(s):
            if char in last_seen:
                start = max(start, last_seen[char])
            last_seen[char] = index
            if index - start >= k:
                count += 1
        return count


if __name__ == "__main__":
    test_cases = [
        ("havefunonleetcode", 5, 6),
        ("home", 5, 0),
        ("awaglknagawunagwkwagl", 4, 13),
        ("aaaa", 1, 4),
        ("abc", 3, 1),
        ("abca", 3, 2),
    ]
    for _, (s, k, expected) in enumerate(test_cases):
        assert Solution().numKLenSubstrNoRepeats(s, k) == expected
