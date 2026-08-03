# @lc app=leetcode.cn id=1585 lang=python3


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        positions = [[] for _ in range(10)]
        for index, digit in enumerate(s):
            positions[int(digit)].append(index)
        used = [0] * 10
        for digit in t:
            value = int(digit)
            if used[value] == len(positions[value]):
                return False
            index = positions[value][used[value]]
            if any(
                positions[smaller]
                and used[smaller] < len(positions[smaller])
                and positions[smaller][used[smaller]] < index
                for smaller in range(value)
            ):
                return False
            used[value] += 1
        return True


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isTransformable, ("84532", "34852"), True),
        (solution.isTransformable, ("12345", "12435"), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1585 题 "检查字符串是否可以通过排序子字符串得到" 所有测试用例通过')
