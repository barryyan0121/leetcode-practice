"""2516. 每种字符至少取 K 个"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = [s.count(char) for char in "abc"]
        if min(total) < k:
            return -1
        left = 0
        window = [0, 0, 0]
        longest = 0
        for right, char in enumerate(s):
            window[ord(char) - 97] += 1
            while any(window[i] > total[i] - k for i in range(3)):
                window[ord(s[left]) - 97] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return len(s) - longest


if __name__ == "__main__":
    test_cases = [(("aabaaaacaabc", 2), 8)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().takeCharacters(*args) == expected
