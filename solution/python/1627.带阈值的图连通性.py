# @lc app=leetcode.cn id=1627 lang=python3


class Solution:
    def areConnected(
        self, n: int, threshold: int, queries: list[list[int]]
    ) -> list[bool]:
        parent = list(range(n + 1))

        def find(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        def union(left: int, right: int) -> None:
            left, right = find(left), find(right)
            if left != right:
                parent[left] = right

        for divisor in range(threshold + 1, n + 1):
            for multiple in range(divisor * 2, n + 1, divisor):
                union(divisor, multiple)
        return [find(left) == find(right) for left, right in queries]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.areConnected, (6, 2, [[1, 4], [2, 5], [3, 6]]), [False, False, True])
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1627 题 "带阈值的图连通性" 所有测试用例通过')
