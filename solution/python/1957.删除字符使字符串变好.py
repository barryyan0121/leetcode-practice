"""1957. 删除字符使字符串变好"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = []
        for char in s:
            if len(answer) < 2 or answer[-1] != char or answer[-2] != char:
                answer.append(char)
        return "".join(answer)


if __name__ == "__main__":
    test_cases = [(("leeetcode",), "leetcode"), (("aaabaaaa",), "aabaa")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().makeFancyString(*args) == expected
