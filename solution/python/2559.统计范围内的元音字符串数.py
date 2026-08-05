"""2559. 统计范围内的元音字符串数"""


class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = set("aeiou")
        prefix = [0]
        for word in words:
            prefix.append(prefix[-1] + (word[0] in vowels and word[-1] in vowels))
        return [prefix[right + 1] - prefix[left] for left, right in queries]


if __name__ == "__main__":
    test_cases = [((["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4]]), [2, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().vowelStrings(*args) == expected
