# @lc app=leetcode.cn id=1694 lang=python3


class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = "".join(char for char in number if char.isdigit())
        groups = []
        while len(digits) > 4:
            groups.append(digits[:3])
            digits = digits[3:]
        if len(digits) == 4:
            groups.extend((digits[:2], digits[2:]))
        else:
            groups.append(digits)
        return "-".join(groups)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.reformatNumber, ("1-23-45 6",), "123-456"),
        (solution.reformatNumber, ("123 4-5678",), "123-456-78"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1694 题 "重新排列数字得到最小值" 所有测试用例通过')
