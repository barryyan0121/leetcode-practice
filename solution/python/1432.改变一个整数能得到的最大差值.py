# @lc app=leetcode.cn id=1432 lang=python3


class Solution:
    def maxDiff(self, num: int) -> int:
        text = str(num)
        high_digit = next((char for char in text if char != "9"), None)
        high = int(text.replace(high_digit, "9")) if high_digit else num
        if text[0] != "1":
            low = int(text.replace(text[0], "1"))
        else:
            low_digit = next((char for char in text[1:] if char not in "01"), None)
            low = int(text.replace(low_digit, "0")) if low_digit else num
        return high - low


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.maxDiff, (555,), 888), (solution.maxDiff, (9,), 8)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1432 题 "改变一个整数能得到的最大差值" 所有测试用例通过')
