from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counts = Counter(text)
        answer = 0
        for char in counts:
            left = different = 0
            for right, value in enumerate(text):
                different += value != char
                while different > 1:
                    different -= text[left] != char
                    left += 1
                answer = max(answer, min(counts[char], right - left + 1))
        return answer


if __name__ == "__main__":
    test_cases = [("ababa", 3), ("aaabaaa", 6), ("aaabbaaa", 4), ("aaaaa", 5)]
    for _, (text, expected) in enumerate(test_cases):
        assert Solution().maxRepOpt1(text) == expected
