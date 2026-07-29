from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        available = Counter(chars)
        return sum(len(word) for word in words if not Counter(word) - available)


if __name__ == "__main__":
    test_cases = [
        (["cat", "bt", "hat", "tree"], "atach", 6),
        (["hello", "world", "leetcode"], "welldonehoneyr", 10),
    ]
    for _, (words, chars, expected) in enumerate(test_cases):
        assert Solution().countCharacters(words, chars) == expected
