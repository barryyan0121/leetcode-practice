from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        count, target, left, answer = Counter(s), len(s) // 4, 0, len(s)
        if all(count[char] <= target for char in "QWER"):
            return 0
        for right, char in enumerate(s):
            count[char] -= 1
            while all(count[char] <= target for char in "QWER"):
                answer = min(answer, right - left + 1)
                count[s[left]] += 1
                left += 1
        return answer


if __name__ == "__main__":
    test_cases = [("QWER", 0), ("QQWE", 1), ("QQQW", 2)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().balancedString(s) == expected
