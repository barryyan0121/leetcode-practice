class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key=lambda word: word[-1])
        return " ".join(word[:-1] for word in words)


if __name__ == "__main__":
    solution = Solution()
    assert solution.sortSentence("is2 sentence4 This1 a3") == "This is a sentence"
    print("1859 passed")
