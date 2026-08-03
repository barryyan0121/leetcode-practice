# @lc app=leetcode.cn id=1566 lang=python3


class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        for start in range(len(arr) - m * k + 1):
            if all(arr[start + i] == arr[start + i % m] for i in range(m * k)):
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.containsPattern, ([1, 2, 4, 4, 4, 4], 1, 3), True),
        (solution.containsPattern, ([1, 2, 1, 2, 1, 1, 1, 3], 2, 2), True),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1566 题 "重复至少 K 次且长度为 M 的模式" 所有测试用例通过')
