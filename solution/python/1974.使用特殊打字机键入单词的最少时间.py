"""1974. 使用特殊打字机键入单词的最少时间"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        answer = len(word)
        previous = "a"
        for char in word:
            distance = abs(ord(char) - ord(previous))
            answer += min(distance, 26 - distance)
            previous = char
        return answer


if __name__ == "__main__":
    test_cases = [(("abc",), 5), (("bza",), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minTimeToType(*args) == expected
