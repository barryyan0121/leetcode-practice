# @lc app=leetcode.cn id=1722 lang=python3


class Solution:
    def minimumHammingDistance(
        self, source: list[int], target: list[int], allowedSwaps: list[list[int]]
    ) -> int:
        from collections import Counter

        parent = list(range(len(source)))

        def find(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        for left, right in allowedSwaps:
            left, right = find(left), find(right)
            parent[left] = right
        groups = {}
        for index, value in enumerate(source):
            groups.setdefault(find(index), Counter())[value] += 1
        answer = 0
        for index, value in enumerate(target):
            group = groups[find(index)]
            if group[value]:
                group[value] -= 1
            else:
                answer += 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.minimumHammingDistance,
            ([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]),
            1,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1722 题 "通过交换数组元素使两个数组相等" 所有测试用例通过')
