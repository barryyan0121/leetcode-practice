class Solution:
    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        banned = set(bannedWords)
        return sum(word in banned for word in message) >= 2


if __name__ == "__main__":
    test_cases = [
        ((["hello", "world", "leetcode"], ["world", "hello"]), True),
        (
            (["hello", "programming", "fun"], ["world", "programming", "leetcode"]),
            False,
        ),
    ]
    for _, ((message, banned_words), expected) in enumerate(test_cases):
        assert Solution().reportSpam(message, banned_words) == expected
