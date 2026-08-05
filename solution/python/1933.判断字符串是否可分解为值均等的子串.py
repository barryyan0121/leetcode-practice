"""1933. 判断字符串是否可分解为值均等的子串"""


class Solution:
    def isDecomposable(self, s: str) -> bool:
        twos = 0
        index = 0
        while index < len(s):
            end = index
            while end < len(s) and s[end] == s[index]:
                end += 1
            length = end - index
            if length % 3 == 1:
                return False
            if length % 3 == 2:
                twos += 1
            index = end
        return twos == 1


if __name__ == "__main__":
    test_cases = [("000111000", False), ("00011111222", True)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().isDecomposable(s) == expected
