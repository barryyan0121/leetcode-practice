"""2416. 字符串的前缀分数和"""


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {"count": 0})
                node["count"] += 1
        answer = []
        for word in words:
            node = trie
            score = 0
            for char in word:
                node = node[char]
                score += node["count"]
            answer.append(score)
        return answer


if __name__ == "__main__":
    test_cases = [((["abc", "ab", "bc", "b"],), [5, 4, 3, 2])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().sumPrefixScores(*args) == expected
