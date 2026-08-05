"""2060. 检查字符串是否可以通过重排得到"""

from functools import lru_cache


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def search(i: int, j: int, difference: int) -> bool:
            if i == len(s1) and j == len(s2):
                return difference == 0
            if difference > 0 and j < len(s2) and s2[j].isalpha():
                return search(i, j + 1, difference - 1)
            if difference < 0 and i < len(s1) and s1[i].isalpha():
                return search(i + 1, j, difference + 1)
            if i < len(s1) and s1[i].isdigit():
                value = 0
                for end in range(i, min(len(s1), i + 3)):
                    if not s1[end].isdigit():
                        break
                    value = value * 10 + int(s1[end])
                    if search(end + 1, j, difference + value):
                        return True
            if j < len(s2) and s2[j].isdigit():
                value = 0
                for end in range(j, min(len(s2), j + 3)):
                    if not s2[end].isdigit():
                        break
                    value = value * 10 + int(s2[end])
                    if search(i, end + 1, difference - value):
                        return True
            if difference == 0 and i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                return search(i + 1, j + 1, 0)
            return False

        return search(0, 0, 0)


if __name__ == "__main__":
    test_cases = [(("internationalization", "i18n"), True), (("l123e", "44"), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().possiblyEquals(*args) == expected
