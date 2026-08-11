class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        counts = [0] * 26
        right = 0
        answer = 0
        for left in range(len(s)):
            while right < len(s) and max(counts) < k:
                counts[ord(s[right]) - ord("a")] += 1
                right += 1
            if max(counts) >= k:
                answer += len(s) - right + 1
            counts[ord(s[left]) - ord("a")] -= 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (("abacb", 2), 4),
        (("abcde", 1), 15),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().numberOfSubstrings(s, k) == expected
