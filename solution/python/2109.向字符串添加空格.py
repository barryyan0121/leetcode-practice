"""2109. 向字符串添加空格"""


class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        previous = 0
        for index in spaces:
            result.extend((s[previous:index], " "))
            previous = index
        result.append(s[previous:])
        return "".join(result)


if __name__ == "__main__":
    test_cases = [(("LeetcodeHelpsMeLearn", [8, 13, 15]), "Leetcode Helps Me Learn")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().addSpaces(*args) == expected
