class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        length = len(word) - numFriends + 1
        return max(
            word[index : index + min(length, len(word) - index)]
            for index in range(len(word))
        )


if __name__ == "__main__":
    test_cases = [
        (("dbca", 2), "dbc"),
        (("gggg", 4), "g"),
        (("aann", 2), "nn"),
    ]
    for _, ((word, num_friends), expected) in enumerate(test_cases):
        assert Solution().answerString(word, num_friends) == expected
