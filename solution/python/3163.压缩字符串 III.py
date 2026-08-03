class Solution:
    def compressedString(self, word: str) -> str:
        answer = []
        index = 0
        while index < len(word):
            end = index + 1
            while end < len(word) and word[end] == word[index] and end - index < 9:
                end += 1
            answer.append(str(end - index))
            answer.append(word[index])
            index = end
        return "".join(answer)


if __name__ == "__main__":
    test_cases = [("abcde", "1a1b1c1d1e"), ("aaaaaaaaaaaaaabb", "9a5a2b")]
    for _, (word, expected) in enumerate(test_cases):
        assert Solution().compressedString(word) == expected
