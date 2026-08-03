# @lc app=leetcode.cn id=1713 lang=python3


class Solution:
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        from bisect import bisect_left

        position = {value: index for index, value in enumerate(target)}
        sequence = [position[value] for value in arr if value in position]
        lis = []
        for value in sequence:
            index = bisect_left(lis, value)
            if index == len(lis):
                lis.append(value)
            else:
                lis[index] = value
        return len(target) - len(lis)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minOperations, ([5, 1, 3], [9, 4, 2, 3, 4]), 2),
        (solution.minOperations, ([6, 4, 8, 1, 3, 2], [4, 7, 6, 2, 3, 8, 6, 1]), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1713 题 "得到子序列的最少操作次数" 所有测试用例通过')
