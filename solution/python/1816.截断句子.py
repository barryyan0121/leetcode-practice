"""1816. 截断句子"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


if __name__ == "__main__":
    test_cases = [(("Hello how are you Contestant", 4), "Hello how are you")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().truncateSentence(*args) == expected
