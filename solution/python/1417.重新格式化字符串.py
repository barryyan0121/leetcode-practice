# @lc app=leetcode.cn id=1417 lang=python3


class Solution:
    def reformat(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        digits = [char for char in s if char.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(letters) < len(digits):
            letters, digits = digits, letters
        result = []
        for index, char in enumerate(letters):
            result.append(char)
            if index < len(digits):
                result.append(digits[index])
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.reformat, ("leetcode",), "")]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    assert solution.reformat("a0b1c2") in {"a0b1c2", "0a1b2c"}
    print('第 1417 题 "重新格式化字符串" 所有测试用例通过')
