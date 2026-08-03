# @lc app=leetcode.cn id=1552 lang=python3


class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()

        def can(distance: int) -> bool:
            count, last = 1, position[0]
            for value in position[1:]:
                if value - last >= distance:
                    count += 1
                    last = value
            return count >= m

        left, right = 1, position[-1] - position[0]
        while left <= right:
            middle = (left + right) // 2
            if can(middle):
                left = middle + 1
            else:
                right = middle - 1
        return right


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxDistance, ([1, 2, 3, 4, 7], 3), 3),
        (solution.maxDistance, ([5, 4, 3, 2, 1, 1000000000], 2), 999999999),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1552 题 "两球之间的磁力" 所有测试用例通过')
