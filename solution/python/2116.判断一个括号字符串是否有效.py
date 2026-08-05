"""2116. 判断一个括号字符串是否有效"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        low = high = 0
        for char, fixed in zip(s, locked):
            if fixed == "0":
                low -= 1
                high += 1
            elif char == "(":
                low += 1
                high += 1
            else:
                low -= 1
                high -= 1
            low = max(low, 0)
            if high < 0:
                return False
        return low == 0


if __name__ == "__main__":
    test_cases = [(("))()))", "010100"), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().canBeValid(*args) == expected
