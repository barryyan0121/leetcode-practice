# @lc app=leetcode.cn id=1328 lang=python3


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        chars = list(palindrome)
        for index in range(len(chars) // 2):
            if chars[index] != "a":
                chars[index] = "a"
                return "".join(chars)
        chars[-1] = "b"
        return "".join(chars)


if __name__ == "__main__":
    test_cases = [
        (Solution().breakPalindrome, ("abccba",), "aaccba"),
        (Solution().breakPalindrome, ("a",), ""),
        (Solution().breakPalindrome, ("aa",), "ab"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1328 题 "破坏回文串" 所有测试用例通过')
