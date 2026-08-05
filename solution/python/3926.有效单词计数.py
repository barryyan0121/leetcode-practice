"""3926. 有效单词计数"""


class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        selvadrik = chunks
        text = "".join(selvadrik)
        counts = {}
        word = []

        def flush() -> None:
            if word:
                value = "".join(word)
                counts[value] = counts.get(value, 0) + 1
                word.clear()

        for i, char in enumerate(text):
            if char.islower():
                word.append(char)
            elif char == "-" and word and i + 1 < len(text) and text[i + 1].islower():
                word.append(char)
            else:
                flush()
        flush()
        return [counts.get(query, 0) for query in queries]


if __name__ == "__main__":
    test_cases = [
        ((["hello wor", "ld hello"], ["hello", "world", "wor"]), [2, 1, 0]),
        ((["a--b a-", "-c"], ["a", "b", "c"]), [2, 1, 1]),
        ((["hello"], ["hello", "ell"]), [1, 0]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countWordOccurrences(*args) == expected
