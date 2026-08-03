# @lc app=leetcode.cn id=1528 lang=python3


class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [""] * len(s)
        for char, index in zip(s, indices):
            result[index] = char
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.restoreString, ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]), "leetcode")
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1528 题 "重新排列字符串" 所有测试用例通过')
