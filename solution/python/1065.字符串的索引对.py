class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node["#"] = True
        answer = []
        for start in range(len(text)):
            node = root
            for end in range(start, len(text)):
                if text[end] not in node:
                    break
                node = node[text[end]]
                if "#" in node:
                    answer.append([start, end])
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            "thestoryofleetcodeandme",
            ["story", "fleet", "leetcode"],
            [[3, 7], [9, 13], [10, 17]],
        ),
        ("ababa", ["aba", "ab"], [[0, 1], [0, 2], [2, 3], [2, 4]]),
    ]
    for _, (text, words, expected) in enumerate(test_cases):
        assert Solution().indexPairs(text, words) == expected
