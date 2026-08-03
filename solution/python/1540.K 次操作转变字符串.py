# @lc app=leetcode.cn id=1540 lang=python3


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        used = [0] * 26
        for first, second in zip(s, t):
            shift = (ord(second) - ord(first)) % 26
            if shift == 0:
                continue
            used[shift] += 1
            if shift + 26 * (used[shift] - 1) > k:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.canConvertString, ("input", "ouput", 9), True)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1540 题 "K 次操作转变字符串" 所有测试用例通过')
