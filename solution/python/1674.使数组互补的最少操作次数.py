# @lc app=leetcode.cn id=1674 lang=python3


class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        changes = [0] * (2 * limit + 2)
        for index in range(len(nums) // 2):
            left, right = nums[index], nums[-index - 1]
            if left > right:
                left, right = right, left
            changes[2] += 2
            changes[left + 1] -= 1
            changes[right + limit + 1] += 1
            changes[left + right] -= 1
            changes[left + right + 1] += 1
        current = 0
        answer = len(nums)
        for value in range(2, 2 * limit + 1):
            current += changes[value]
            answer = min(answer, current)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minMoves, ([1, 2, 4, 3], 4), 1),
        (solution.minMoves, ([1, 2, 2, 1], 2), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1674 题 "使数组互补的最少操作次数" 所有测试用例通过')
