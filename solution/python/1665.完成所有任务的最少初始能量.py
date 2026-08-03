# @lc app=leetcode.cn id=1665 lang=python3


class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda task: task[1] - task[0], reverse=True)
        energy = answer = 0
        for actual, minimum in tasks:
            answer = max(answer, energy + minimum)
            energy += actual
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minimumEffort, ([[1, 2], [2, 4], [4, 8]],), 8),
        (solution.minimumEffort, ([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]],), 32),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1665 题 "完成所有任务的最少初始能量" 所有测试用例通过')
