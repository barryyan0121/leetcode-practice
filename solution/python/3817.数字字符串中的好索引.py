"""3817. 数字字符串中的好索引"""


class Solution:
    def goodIndices(self, s: str) -> list[int]:
        answer = []
        for index in range(len(s)):
            text = str(index)
            if s[max(0, index - len(text) + 1) : index + 1] == text:
                answer.append(index)
        return answer


if __name__ == "__main__":
    test_cases = [(("0234567890112",), [0, 11, 12]), (("01234",), [0, 1, 2, 3, 4])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().goodIndices(*args) == expected
