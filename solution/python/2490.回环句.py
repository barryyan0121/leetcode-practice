"""2490. 回环句"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        return all(
            words[index][-1] == words[(index + 1) % len(words)][0]
            for index in range(len(words))
        )


if __name__ == "__main__":
    assert Solution().isCircularSentence("leetcode exercises sound delightful")
