class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = {}
        left = 0
        answer = 0
        for right, character in enumerate(s):
            counts[character] = counts.get(character, 0) + 1
            while counts[character] > 2:
                counts[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    test_cases = [("bcbbbcba", 4), ("aaaa", 2)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().maximumLengthSubstring(s) == expected
