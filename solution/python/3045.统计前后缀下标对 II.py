class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        trie = {}
        answer = 0
        for word in words:
            node = trie
            for left, right in zip(word, reversed(word)):
                node = node.setdefault((left, right), {})
                answer += node.get("count", 0)
            node["count"] = node.get("count", 0) + 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (["a", "a"], 1),
        (["a", "ab", "aba"], 1),
        (["pa", "papa", "ma", "mama"], 2),
    ]
    for _, (words, expected) in enumerate(test_cases):
        assert Solution().countPrefixSuffixPairs(words) == expected
